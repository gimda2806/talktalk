#!/usr/bin/env python3
"""제타 플롯 md 파일을 휴대폰에서 칸별로 복사할 수 있는 HTML 페이지로 바꾼다.

사용법: python3 zeta/tools/make_copy_page.py <플롯.md> <설정집.md> <출력.html> <캐릭터이름>
출력 HTML은 Artifact 도구로 게시한다. (복사 버튼은 클릭 핸들러에서 clipboard.writeText를 호출한다.)
"""
import re, sys, json

TEMPLATE = '<title>__NAME__ 입력 도우미</title>\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&display=swap">\n<style>\n:root{--bg:#f4f5f7;--card:#ffffff;--fg:#1b2230;--muted:#667085;--line:#dfe3ea;--accent:#1f3a5f;--accent-fg:#ffffff;--ok:#1f7a4d;--tab:#e8ecf3}\n@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#10141c;--card:#181e2a;--fg:#e8eaf0;--muted:#98a2b3;--line:#2a3345;--accent:#8fb0e0;--accent-fg:#10141c;--ok:#5ec28d;--tab:#222b3b;color-scheme:dark}}\n:root[data-theme="dark"]{--bg:#10141c;--card:#181e2a;--fg:#e8eaf0;--muted:#98a2b3;--line:#2a3345;--accent:#8fb0e0;--accent-fg:#10141c;--ok:#5ec28d;--tab:#222b3b;color-scheme:dark}\nbody{background:var(--bg);color:var(--fg);font-family:\'Noto Sans KR\',system-ui,sans-serif;line-height:1.6;padding-inline:16px}\nmain{max-width:720px;margin:0 auto;padding-block:20px 80px}\nh1{font-size:1.25rem;margin:0 0 4px}\n.sub{color:var(--muted);font-size:.85rem;margin:0 0 14px}\nnav{position:sticky;top:env(safe-area-inset-top,0px);z-index:2;background:var(--bg);padding-block:8px;display:flex;gap:6px;overflow-x:auto}\nnav button{flex:0 0 auto;border:1px solid var(--line);background:var(--tab);color:var(--fg);border-radius:99px;padding:8px 16px;font:inherit;font-size:.9rem}\nnav button[aria-selected="true"]{background:var(--accent);color:var(--accent-fg);border-color:var(--accent);font-weight:700}\n.card{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:12px 14px;margin-top:12px;min-width:0}\n.top{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:8px}\n.lab{font-weight:700;font-size:.92rem;min-width:0;overflow-wrap:anywhere}\n.n{color:var(--muted);font-size:.78rem;font-variant-numeric:tabular-nums;white-space:nowrap}\n.copy{flex:0 0 auto;min-width:76px;min-height:44px;border:0;border-radius:8px;background:var(--accent);color:var(--accent-fg);font:inherit;font-weight:700;font-size:.95rem}\n.copy.done{background:var(--ok);color:#fff}\npre{margin:0;white-space:pre-wrap;overflow-wrap:anywhere;font:inherit;font-size:.86rem;max-height:9.5em;overflow:hidden;position:relative;-webkit-user-select:text;user-select:text}\npre.open{max-height:none}\n.more{margin-top:6px;border:0;background:none;color:var(--accent);font:inherit;font-size:.82rem;padding:4px 0}\n</style>\n<main>\n<h1>__NAME__ 입력 도우미</h1>\n<p class="sub">칸마다 복사 버튼을 누르고 제타 입력 칸에 붙여 넣으세요. 줄바꿈과 별표는 그대로 복사됩니다.</p>\n<nav id="tabs" role="tablist"></nav>\n<section id="list"></section>\n</main>\n<script>\nconst DATA=__DATA__;\nconst tabs=document.getElementById(\'tabs\'),list=document.getElementById(\'list\');\nlet cur=0;\ntry{const s=sessionStorage.getItem(\'tab\');if(s!==null)cur=Math.min(+s||0,DATA.length-1)}catch(e){}\nfunction fallback(el){const r=document.createRange();r.selectNodeContents(el);const s=getSelection();s.removeAllRanges();s.addRange(r)}\nasync function copy(btn,text,pre){\n  try{await navigator.clipboard.writeText(text);btn.textContent=\'복사됨\';btn.classList.add(\'done\')}\n  catch(e){pre.classList.add(\'open\');fallback(pre);btn.textContent=\'선택됨\';btn.classList.add(\'done\')}\n  setTimeout(()=>{btn.textContent=\'복사\';btn.classList.remove(\'done\')},1800)\n}\nfunction render(){\n  tabs.innerHTML=\'\';list.innerHTML=\'\';\n  DATA.forEach((d,i)=>{const b=document.createElement(\'button\');b.textContent=d.tab;b.setAttribute(\'role\',\'tab\');b.setAttribute(\'aria-selected\',i===cur);b.onclick=()=>{cur=i;try{sessionStorage.setItem(\'tab\',i)}catch(e){}render();scrollTo(0,0)};tabs.appendChild(b)});\n  DATA[cur].items.forEach(it=>{\n    const c=document.createElement(\'div\');c.className=\'card\';\n    const top=document.createElement(\'div\');top.className=\'top\';\n    const l=document.createElement(\'div\');l.className=\'lab\';l.textContent=it.label;\n    const n=document.createElement(\'span\');n.className=\'n\';n.textContent=it.n+\'자\';\n    const left=document.createElement(\'div\');left.style.minWidth=\'0\';left.append(l,n);\n    const btn=document.createElement(\'button\');btn.className=\'copy\';btn.textContent=\'복사\';\n    top.append(left,btn);\n    const pre=document.createElement(\'pre\');pre.textContent=it.text;\n    btn.onclick=()=>copy(btn,it.text,pre);\n    c.append(top,pre);\n    if(it.text.split(\'\\n\').length>7||it.n>260){const m=document.createElement(\'button\');m.className=\'more\';m.textContent=\'전체 보기\';m.onclick=()=>{pre.classList.toggle(\'open\');m.textContent=pre.classList.contains(\'open\')?\'접기\':\'전체 보기\'};c.append(m)}\n    list.appendChild(c)\n  })\n}\nrender();\n</script>\n'


def blocks(text):
    lines = text.split('\n')
    out, sec, head, label, i = [], '', '', '', 0
    while i < len(lines):
        l = lines[i]
        if l.startswith('## '):
            sec, head = l[3:].strip(), ''
        elif l.startswith('### ') or l.startswith('#### '):
            head, label = l.lstrip('#').strip(), ''
        elif l.strip() in ('제목', '키워드', '내용'):
            label = l.strip()
        elif l.startswith('```text'):
            j, buf = i + 1, []
            while not lines[j].startswith('```'):
                buf.append(lines[j]); j += 1
            out.append((sec, head, label, '\n'.join(buf)))
            label, i = '', j
        i += 1
    return out


def clean(h):
    return re.sub(r"\s*\(.*?\)", "", h).replace('`', '').strip()


def build(plot_md, lore_md):
    tabs = {'프롬프트': [], '인트로': [], '소개': [], '설정집': [], '이미지': []}
    image_names = {'주인공 프로필용': '주인공 프로필', '남성용': '유저 프로필 · 남성용', '여성용': '유저 프로필 · 여성용', '유저 대화 프로필용': '유저 프로필'}
    for sec, head, label, text in blocks(plot_md):
        h = clean(head)
        if sec.startswith('1.'):
            tabs['프롬프트'].append((h, text))
        elif sec.startswith('2.'):
            tabs['인트로'].append(('① 대화 프로필 선택 시점' if h.startswith('①') else '②~⑥ 인트로 (한 번에 붙여넣기)', text))
        elif sec.startswith('3.'):
            tabs['소개'].append(('소개글', text))
        elif sec.startswith('5.'):
            tabs['이미지'].append((image_names.get(h, h), text))
    count = {}
    for sec, head, label, text in blocks(lore_md):
        h = head.strip()
        if h.startswith('항목'):
            n = count.get(h, 0); count[h] = n + 1
            tabs['설정집'].append((f"{h} · {['제목', '키워드', '내용'][n]}", text))
        else:
            tabs['설정집'].append((h, text))
    return [{'tab': k, 'items': [{'label': a, 'text': b, 'n': len(b)} for a, b in v]} for k, v in tabs.items() if v]


if __name__ == '__main__':
    plot, lore, out, name = sys.argv[1:5]
    data = build(open(plot, encoding='utf-8').read(), open(lore, encoding='utf-8').read())
    html = TEMPLATE.replace('__DATA__', json.dumps(data, ensure_ascii=False).replace('</', '<\\/')).replace('__NAME__', name)
    open(out, 'w', encoding='utf-8').write(html)
    print(out, sum(len(d['items']) for d in data), '칸')
