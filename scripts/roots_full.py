#!/usr/bin/env python3
"""Root every remaining form. Model proposes; a deterministic rule grades."""
import json,os,re,time,collections,requests
from concurrent.futures import ThreadPoolExecutor
from dotenv import load_dotenv
load_dotenv(os.path.expanduser("~/global-infra/sefer-mcp/.env"))
K=os.environ["OPENROUTER_API_KEY"]; MODEL="google/gemini-2.5-flash-lite"
NIK=re.compile(r'[֑-ׇ]'); FIN={'ך':'כ','ם':'מ','ן':'נ','ף':'פ','ץ':'צ'}
strip=lambda s: NIK.sub('',s or '')
canon=lambda s: ''.join(FIN.get(c,c) for c in strip(s))
WEAK=set('נוימה')
def grade(word,root):
    w=canon(word); L=canon(root).replace('-','')
    if len(L)<2 or len(L)>4: return "reject"
    i=0; miss=[]
    for ch in L:
        j=w.find(ch,i)
        if j<0: miss.append(ch)
        else: i=j+1
    if not miss: return "verified"
    if len(miss)==1 and miss[0] in WEAK: return "weak"
    if len(miss)==1 and len(L)>2 and L[1]==L[2]: return "weak"
    if len(miss)==1 and miss[0] in "יו":
        alt=w.replace("ו","י") if miss[0]=="י" else w.replace("י","ו")
        i2=0
        if all((lambda j: (j>=0))(alt.find(ch,i2)) for ch in L): return "weak"
    return "reject"
todo=json.load(open("todo_forms.json",encoding="utf-8"))
SYS=("You give the Hebrew triliteral root (shoresh) of a single word from the siddur. "
     "This is liturgical/biblical Hebrew, not modern. Reply with ONLY the root as letters "
     "separated by hyphens, e.g. מ-ל-כ . If the word is a particle, proper name, number, or "
     "has no root, reply exactly: NONE")
def one(f):
    for _ in range(3):
        try:
            r=requests.post("https://openrouter.ai/api/v1/chat/completions",
              headers={"Authorization":f"Bearer {K}","Content-Type":"application/json"},
              json={"model":MODEL,"temperature":0,"max_tokens":24,
                    "messages":[{"role":"system","content":SYS},{"role":"user","content":f}]},
              timeout=60)
            if r.status_code!=200: time.sleep(1.5); continue
            j=r.json()
            return f,j["choices"][0]["message"]["content"].strip(),j.get("usage",{})
        except Exception: time.sleep(1.5)
    return f,None,{}
t0=time.time(); out={}; tal=collections.Counter(); pt=ct=0
with ThreadPoolExecutor(24) as ex:
    for n,(f,t,u) in enumerate(ex.map(one,todo),1):
        pt+=u.get("prompt_tokens",0); ct+=u.get("completion_tokens",0)
        if n%2000==0: print(f"    {n:,}/{len(todo):,}  {time.time()-t0:.0f}s",flush=True)
        if not t: tal["error"]+=1; continue
        if t.upper().startswith("NONE"): tal["none"]+=1; out[f]={"root":None,"basis":"none"}; continue
        root=re.sub(r'[^֐-ת-]','',t).strip('-')
        if not root: tal["unparsed"]+=1; continue
        g=grade(f,root); tal[g]+=1
        out[f]={"root":root if g!="reject" else None,"basis":g,"raw":root}
json.dump(out,open("roots_full.json","w",encoding="utf-8"),ensure_ascii=False)
print(f"  {len(todo):,} forms · {time.time()-t0:.0f}s · {pt:,}+{ct:,} tok · ${pt/1e6*0.10+ct/1e6*0.40:.3f}")
for k,v in tal.most_common(): print(f"    {k:10} {v:>6}")
