#!/usr/bin/env python3
"""Build the course in the user's ORIGINAL single-file SPA format (course/Enterprise_Network_Course_Lessons.html):
window.COURSE={version,updated,modules,review,lessons{id:{sub,html}}} + the original renderer (sidebar accordion, fonts, sizes, 3 themes, progress)."""
import re,sys,glob,os,base64,html as H,markdown
src=sys.argv[1]; out=sys.argv[2]; ver=sys.argv[3]; upd=sys.argv[4]
TPL='/home/user/01-FGT/course/Enterprise_Network_Course_Lessons.html'
tpl=open(TPL).read()
figdir=os.path.join(os.path.dirname(src.rstrip('/')),'figures')

FA=str.maketrans('0123456789','۰۱۲۳۴۵۶۷۸۹')
def fa_prefix(s):
    # convert digits only in the leading 'درس N-M' / 'فصل N' / 'بخش N' identifiers
    return re.sub(r'^(درس|فصل|بخش)\s+([0-9][0-9\-]*)',lambda m:m.group(1)+' '+m.group(2).translate(FA),s)
def esc(s): return s.replace('\\','\\\\').replace('`','\\`').replace('${','\\${')
def fenced_lines(text):
    infence=False
    for ln in text.split('\n'):
        if re.match(r'^```',ln): infence=not infence; yield ln,False; continue
        yield ln,(not infence)
def split_blocks(text):
    """yield (level,title,body) for h1/h2 outside fences; body excludes the heading line."""
    blocks=[];cur=[0,'',[]]
    for ln,live in fenced_lines(text):
        m=re.match(r'^(#{1,2}) (.+)$',ln) if live else None
        if m:
            blocks.append(cur); cur=[len(m.group(1)),m.group(2).strip(),[]]
        else: cur[2].append(ln)
    blocks.append(cur)
    return [(l,t,'\n'.join(b).strip()) for l,t,b in blocks if l or '\n'.join(b).strip()]

def img(m):
    alt,path=m.group(1),m.group(2); fp=os.path.normpath(os.path.join(src,path))
    if os.path.exists(fp):
        return '![%s](data:image/svg+xml;base64,%s)'%(alt,base64.b64encode(open(fp,'rb').read()).decode())
    return m.group(0)

def to_html(md,shift=True):
    md=re.sub(r'(?m)^```\s+(\w+)\s*$',r'```\1',md)
    md=re.sub(r'!\[([^\]]*)\]\(([^)\s]+\.svg)\)',img,md)
    md=re.sub(r'(?m)^\*شکل[^\n]*\*\s*$','',md)           # duplicated caption line
    md=re.sub(r'<!--.*?-->','',md,flags=re.S)
    md=re.sub(r'<a id="[^"]*"></a>','',md)
    h=markdown.markdown(md,extensions=['tables','fenced_code','sane_lists'],output_format='html5')
    if shift:
        for a,b in ((5,4),(4,3),(3,2)):
            h=re.sub(r'<h%d>(.*?)</h%d>'%(a,a),r'<h%d>\1</h%d>'%(b,b),h,flags=re.S)
    # blockquote -> .box
    def bq(m):
        inner=m.group(1); cls='box'
        if re.search(r'وضعیت|هشدار',inner[:80]): cls='box warn'
        elif 'یادداشت علمی' in inner[:60] or 'وضعیت منبع' in inner[:60]: cls='box review'
        return '<div class="%s">%s</div>'%(cls,inner)
    h=re.sub(r'<blockquote>(.*?)</blockquote>',bq,h,flags=re.S)
    # figures
    h=re.sub(r'<p><img alt="([^"]*)" src="(data:[^"]+)"\s*/?></p>',r'<figure class="fig"><img src="\2" alt="\1" style="width:100%;background:#fff;border-radius:8px"><figcaption>\1</figcaption></figure>',h)
    # internal lesson links  #l-9-4 -> #/l-9-4
    h=re.sub(r'href="#(l-[\w\-]+)"',r'href="#/\1"',h)
    # meta line
    m=re.match(r'\s*<p><strong>(فصل[^<]*)</strong></p>',h)
    if m:
        tags=''.join('<span class="tag">%s</span>'%re.sub(r'(?<=فصل )[0-9]+',lambda mm:mm.group(0).translate(FA),t.strip()) for t in m.group(1).split('·') if t.strip())
        h='<div class="meta">%s</div>'%tags+h[m.end():]
    return h

modules=[];lessons={}
parts=sorted(glob.glob(os.path.join(src,'Course_Part_*.md')))
pending_head=None
cur_mod=None
def add_page(mod,pid,title,html_body,sub=''):
    mod['lessons'].append({'id':pid,'title':title}); lessons[pid]={'sub':sub,'html':html_body}
for p in parts:
    pn=int(re.search(r'Part_(\d+)',p).group(1))
    blocks=split_blocks(open(p).read())
    head_md=[]; last_mod=None
    i=0
    while i<len(blocks):
        lvl,t,b=blocks[i]
        if lvl==1 and t.startswith('Enterprise Network'):
            j=i+1; body=[b]
            while j<len(blocks) and not (blocks[j][0]==1):
                body.append('## '+blocks[j][1]+'\n\n'+blocks[j][2]); j+=1
            head_md=['\n\n'.join(body)]; pending_head=(pn,'\n\n'.join(body)); i=j; continue
        if lvl==1 and re.match(r'فصل\s*(\d+)',t):
            n=int(re.match(r'فصل\s*(\d+)',t).group(1))
            cur_mod={'id':'c%d'%n,'title':fa_prefix(t),'lessons':[]}; modules.append(cur_mod); last_mod=cur_mod
            if pending_head:
                add_page(cur_mod,'p%d-head'%pending_head[0],'سرآیند بخش '+str(pending_head[0]).translate(FA),to_html(pending_head[1],shift=False)); pending_head=None
            j=i+1
            add_page(cur_mod,'c%d-map'%n,fa_prefix('فصل %d'%n)+' — نقشه و یادداشت علمی',to_html(b) if b else '<p>بدون توضیح.</p>',sub=t)
            i+=1; continue
        if lvl==2 and t.startswith('درس '):
            m=re.match(r'درس\s+(\S+)\s+—\s+(.*)',t); lid='l-'+m.group(1)
            add_page(cur_mod,lid,fa_prefix('درس %s'%m.group(1))+' — '+m.group(2),to_html(b),sub='')
            i+=1; continue
        if lvl==2 and t.startswith('پاسخ‌های'):
            n=int(re.search(r'(\d+)',t).group(1)) if re.search(r'(\d+)',t) else 0
            add_page(cur_mod,'a%d'%n,fa_prefix(t).replace('فصل ','فصل ',1),to_html(b)); i+=1; continue
        if lvl==1 and t.startswith('پایان بخش'):
            j=i+1; body=[b]
            while j<len(blocks) and blocks[j][0]==2:
                body.append('## '+blocks[j][1]+'\n\n'+blocks[j][2]); j+=1
            add_page(last_mod,'p%d-end'%pn,re.sub(r'[0-9]+',lambda m:m.group(0).translate(FA),t),to_html('\n\n'.join(body),shift=False)); i=j; continue
        # stray block: append to last page of current module
        if cur_mod and cur_mod['lessons']:
            lid=cur_mod['lessons'][-1]['id']; lessons[lid]['html']+=to_html(('## '+t+'\n\n' if lvl else '')+b); 
        i+=1

# guide + reports module
def md_file(name): return open(os.path.join(src,name)).read()
guide='''<div class="meta"><span class="tag">راهنما</span><span class="tag">نسخه %s</span></div>
<h2>این فایل چیست؟</h2>
<p>متن کامل دوره‌ی <b>شبکه و امنیت سازمانی</b> (۳۲ فصل، ۲۴۷ درس) در همان قالب تک‌فایلی اولیه: فهرست دروس در سمت راست، هر بار یک درس، پیشرفت مطالعه و سه تم.</p>
<h2>امکانات</h2>
<ul><li><b>☰</b>: مخفی/نمایان‌کردن منوی دروس (در دسکتاپ انتخاب شما ذخیره می‌شود).</li>
<li><b>فونت و اندازه</b> و سه تم 🌙 ☀️ 🌾 در نوار بالا.</li>
<li>هر فصل یک گروه در منو است: «نقشه و یادداشت علمی»، دروس، و «پاسخ‌ها».</li>
<li>دکمه‌ی «علامت‌گذاری به‌عنوان مطالعه‌شده» پیشرفت را در مرورگر ذخیره می‌کند.</li></ul>
<div class="box warn"><b class="t">وضعیت صادقانه</b>هیچ Labی اجرا نشده و دستورها <code>Unverified</code> هستند. بسیاری از ادعاهای مربوط به FortiOS «نیازمند تأیید» ثبت شده‌اند؛ گزارش‌های همین بخش را بخوانید.</div>
<div class="box review"><b class="t">گزارش‌ها</b>در منوی «شروع و راهنما» گزارش اصلاح علمی v4.1 و گزارش تعمیق v4.2 آمده است.</div>
'''%ver
m0={'id':'m0','title':'شروع و راهنما','lessons':[]}
add_page(m0,'guide','راهنمای استفاده از این فایل',guide)
for pid,fn,title in (('rep41','Final_Correction_Report_v4.1.md','گزارش اصلاحات علمی v4.1'),('rep42','Deepening_Report_v4.2.md','گزارش تعمیق ۲۰ درس v4.2')):
    if os.path.exists(os.path.join(src,fn)):
        body=md_file(fn); body=re.sub(r'(?m)^# .*\n','',body,count=1)
        add_page(m0,pid,title,to_html(body))
modules.insert(0,m0)
modules.append({'id':'rv','title':'مرور دوره‌ای','lessons':[{'id':'review','title':'اشتباهات و سؤال‌های من (مرور)'}]})

# review array copied verbatim from the original file
rv=re.search(r'  review: \[.*?\n  \],\n',tpl,re.S).group(0)
def jsq(s): return '"'+s.replace('\\','\\\\').replace('"','\\"')+'"'
mods_js='[\n'+',\n'.join('    {id:%s, title:%s, lessons:[\n%s\n    ]}'%(jsq(m['id']),jsq(m['title']),',\n'.join('      {id:%s, title:%s, ready:true}'%(jsq(l['id']),jsq(l['title'])) for l in m['lessons'])) for m in modules)+'\n  ]'
les_js=',\n'.join('    %s: {sub:%s, html:`%s`}'%(jsq(k),jsq(v['sub']),esc(v['html'])) for k,v in lessons.items())
data='<script id="course-data">\nwindow.COURSE = {\n  version: %s,\n  updated: %s,\n  modules: %s,\n%s  lessons: {\n%s\n  }\n};\n</script>'%(jsq(ver),jsq(upd),mods_js,rv,les_js)
res=re.sub(r'<script id="course-data">.*?</script>',lambda m:data,tpl,count=1,flags=re.S)
res=res.replace("const open=m.lessons.some(l=>l.id===cur)||m.lessons.some(l=>l.ready);","const open=m.lessons.some(l=>l.id===cur);")
open(out,'w').write(res)
print(len(res)//1024,'KB; modules',len(modules),'pages',len(lessons),'lessons',sum(1 for k in lessons if k.startswith('l-')))
