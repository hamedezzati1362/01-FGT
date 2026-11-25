#!/usr/bin/env python3
"""Checks a 3-chapter course Markdown file: internal links, images, answer coverage,
raw HTML leftovers, Persian text inside code fences, referenced repo files.
Usage: python3 tools/check_part.py course/Course_Part_01_Chapters_01-03.md"""
import re, sys, os
p = sys.argv[1]
base = os.path.dirname(os.path.abspath(p))
root = os.path.dirname(os.path.abspath(os.path.join(os.path.dirname(__file__))))
t = open(p, encoding='utf-8').read()
bad = 0
ids = set(re.findall(r'<a id="([^"]+)"></a>', t))
links = re.findall(r'\]\(#([^)]+)\)', t)
broken = [l for l in links if l not in ids]
print(f'anchors={len(ids)} internal_links={len(links)} broken={broken}'); bad += len(broken)
imgs = re.findall(r'!\[[^\]]*\]\(([^)]+)\)', t)
miss = [i for i in imgs if not os.path.exists(os.path.join(base, i))]
print(f'images={len(imgs)} missing={miss}'); bad += len(miss)
refs = set(re.findall(r'پاسخ: ([^ ]+) در بخش', t))
ans = set(re.findall(r'\*\*([^\s*]+-[تمQ]\d+)\*\*', t))
print(f'answer_refs={len(refs)} answers={len(ans)} missing={sorted(refs-ans)}'); bad += len(refs-ans)
html = {k: t.count(k) for k in ['<div', '<span', '<details', '<table', '<br', '<svg', 'FIGMARK', 'ZZFIG']}
print('raw_html', html); bad += sum(html.values())
infence = False; pers = 0
for l in t.split('\n'):
    if l.startswith('```'): infence = not infence; continue
    if infence and re.search('[؀-ۿ]', l): pers += 1
print('persian_in_code_lines', pers); bad += pers
# referenced repo files (inline code with a known extension)
cands = set(re.findall(r'`([A-Za-z0-9_\-./*]+\.(?:md|sh|html|svg|ps1|drawio))`', t))
exist, missing = [], []
for c in sorted(cands):
    if '*' in c: continue
    (exist if os.path.exists(os.path.join(root, c)) or os.path.exists(os.path.join(base, c)) else missing).append(c)
print('referenced_existing', len(exist)); print('referenced_not_in_repo (student outputs or absent):', missing)
print('RESULT', 'FAIL' if bad else 'OK'); sys.exit(1 if bad else 0)
