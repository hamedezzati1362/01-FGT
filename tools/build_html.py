#!/usr/bin/env python3
"""Build a single self-contained RTL HTML from course/vX/Course_Part_*.md (menu toggle, 3 themes, inline SVG figures)."""
import re,sys,glob,base64,os,html,markdown
src=sys.argv[1]; out=sys.argv[2]; title=sys.argv[3] if len(sys.argv)>3 else 'Course'
figdir=os.path.join(os.path.dirname(src.rstrip('/')),'figures')
parts=sorted(glob.glob(os.path.join(src,'Course_Part_*.md')))
md='\n\n'.join(open(p).read().strip() for p in parts)
md=re.sub(r'(?m)^```\s+(\w+)\s*$',r'```\1',md)
def img(m):
    alt,path=m.group(1),m.group(2); fp=os.path.normpath(os.path.join(src,path))
    if os.path.exists(fp):
        d=base64.b64encode(open(fp,'rb').read()).decode()
        return '![%s](data:image/svg+xml;base64,%s)'%(alt,d)
    return m.group(0)
md=re.sub(r'!\[([^\]]*)\]\(([^)\s]+\.svg)\)',img,md)
body=markdown.markdown(md,extensions=['tables','fenced_code','sane_lists'],output_format='html5')
# ids for h1/h2 and TOC
toc=[];n=[0,0]
def h(m):
    lvl,txt=m.group(1),m.group(2)
    if lvl=='1': n[0]+=1; i='ch%d'%n[0]; toc.append((1,i,re.sub('<[^>]+>','',txt)))
    else: n[1]+=1; i='ls%d'%n[1]; toc.append((2,i,re.sub('<[^>]+>','',txt)))
    return '<h%s id="%s">%s</h%s>'%(lvl,i,txt,lvl)
body=re.sub(r'<h([12])>(.*?)</h\1>',h,body,flags=re.S)
nav=[]
for lvl,i,t in toc:
    if (lvl==1 and not t.startswith('فصل')) or (lvl==2 and not t.startswith('درس')): continue
    if lvl==1: nav.append('<div class="nch">%s</div>'%html.escape(t))
    else: nav.append('<a class="nls" href="#%s">%s</a>'%(i,html.escape(t)))
CSS='''
:root{--bg:#10151c;--fg:#e6edf3;--mut:#9aa7b4;--card:#18202a;--bd:#2b3644;--ac:#58a6ff;--code:#0b0f14}
[data-theme=light]{--bg:#fff;--fg:#1f2328;--mut:#59636e;--card:#f6f8fa;--bd:#d0d7de;--ac:#0969da;--code:#f0f3f6}
[data-theme=soft]{--bg:#f4ecd8;--fg:#3b3226;--mut:#6b5d49;--card:#ece0c6;--bd:#cdbd98;--ac:#8a5a14;--code:#e6d9bc}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.9 "Vazirmatn","Tahoma","Segoe UI",sans-serif}
#top{position:fixed;top:0;inset-inline:0;height:48px;background:var(--card);border-bottom:1px solid var(--bd);display:flex;gap:10px;align-items:center;padding:0 12px;z-index:5}
#top b{flex:1;overflow:hidden;white-space:nowrap;text-overflow:ellipsis;font-size:14px}
button,select{background:var(--bg);color:var(--fg);border:1px solid var(--bd);border-radius:6px;padding:4px 10px;font:inherit;cursor:pointer}
#side{position:fixed;top:48px;bottom:0;right:0;width:340px;overflow:auto;background:var(--card);border-left:1px solid var(--bd);padding:10px;z-index:4}
#side input{width:100%;margin-bottom:8px;padding:6px;background:var(--bg);color:var(--fg);border:1px solid var(--bd);border-radius:6px}
.nch{font-weight:700;margin:12px 0 4px;color:var(--ac);font-size:14px}
.nls{display:block;padding:3px 8px;color:var(--fg);text-decoration:none;font-size:13px;line-height:1.6;border-radius:4px}
.nls:hover,.nls.on{background:var(--bg);color:var(--ac)}
main{margin:48px 340px 0 0;padding:20px 28px;max-width:1100px}
body.nomenu #side{display:none}body.nomenu main{margin-right:auto;margin-left:auto}
@media(max-width:900px){#side{width:85%}main{margin-right:0;padding:14px}body:not(.menu) #side{display:none}}
h1{border-bottom:2px solid var(--ac);padding-bottom:6px;margin-top:2.5em}
h2{margin-top:2.2em;border-bottom:1px solid var(--bd);padding-bottom:4px}
h3{margin-top:1.6em;color:var(--ac)}
pre{direction:ltr;text-align:left;background:var(--code);border:1px solid var(--bd);border-radius:8px;padding:12px;overflow:auto;font:13px/1.55 Consolas,"Courier New",monospace}
code{direction:ltr;unicode-bidi:isolate;background:var(--code);padding:1px 5px;border-radius:4px;font:0.9em Consolas,monospace}
pre code{background:none;padding:0}
table{border-collapse:collapse;display:block;overflow:auto;margin:12px 0}
th,td{border:1px solid var(--bd);padding:6px 10px;text-align:right;vertical-align:top}
th{background:var(--card)}
blockquote{margin:12px 0;padding:8px 14px;background:var(--card);border-right:4px solid var(--ac);border-radius:6px;color:var(--mut)}
img{max-width:100%;background:#fff;border-radius:6px;padding:4px}
a{color:var(--ac)}
'''
JS='''
const B=document.body,s=(k,v)=>{try{localStorage.setItem(k,v)}catch(e){}},g=k=>{try{return localStorage.getItem(k)}catch(e){return null}};
const th=g('theme')||'dark';document.documentElement.dataset.theme=th;document.getElementById('th').value=th;
document.getElementById('th').onchange=e=>{document.documentElement.dataset.theme=e.target.value;s('theme',e.target.value)};
const wide=matchMedia('(min-width:901px)').matches;
if(wide){if(g('menu')==='0')B.classList.add('nomenu')}else{B.classList.remove('menu')}
document.getElementById('mb').onclick=()=>{if(wide){B.classList.toggle('nomenu');s('menu',B.classList.contains('nomenu')?'0':'1')}else B.classList.toggle('menu')};
document.getElementById('q').oninput=e=>{const v=e.target.value.trim();document.querySelectorAll('#side .nls').forEach(a=>a.style.display=!v||a.textContent.includes(v)?'':'none')};
'''
doc='''<!doctype html><html lang="fa" dir="rtl" data-theme="dark"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>%s</title><style>%s</style></head><body>
<div id="top"><button id="mb" title="منو">☰</button><b>%s</b><select id="th"><option value="dark">تاریک</option><option value="light">روشن</option><option value="soft">ملایم</option></select></div>
<nav id="side"><input id="q" placeholder="جست‌وجو در درس‌ها">%s</nav><main>%s</main><script>%s</script></body></html>'''%(html.escape(title),CSS,html.escape(title),'\n'.join(nav),body,JS)
open(out,'w').write(doc); print(len(doc)//1024,'KB',n)
