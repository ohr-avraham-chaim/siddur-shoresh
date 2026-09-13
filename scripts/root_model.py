#!/usr/bin/env python3
"""Propose a root for each unrooted form; grade it deterministically."""
import json,os,re,collections,requests,time
from concurrent.futures import ThreadPoolExecutor
from dotenv import load_dotenv
load_dotenv(os.path.expanduser("~/global-infra/sefer-mcp/.env"))
K=os.environ["OPENROUTER_API_KEY"]; MODEL="google/gemini-2.5-flash-lite"
NIK=re.compile(r'[֑-ׇ]'); FIN={'ך':'כ','ם':'מ','ן':'נ','ף':'פ','ץ':'צ'}
strip=lambda s: NIK.sub('',s or '')
canon=lambda s: ''.join(FIN.get(c,c) for c in strip(s))
WEAK=set('נוימה')
def grade(word,root):
    w=canon(word); letters=canon(root).replace('-','')
    if len(letters)<2: return "reject"
    i=0; missing=[]
    for ch in letters:
        j=w.find(ch,i)
        if j<0: missing.append(ch)
        else: i=j+1
    if not missing: return "verified"
    if len(missing)==1 and missing[0] in WEAK: return "weak"   # pe-nun, hollow, lamed-heh
    if len(missing)==1 and len(letters)>2 and letters[1]==letters[2]: return "weak"
    if len(missing)==1 and missing[0] in "יו":
        alt = w.replace("ו","י") if missing[0]=="י" else w.replace("י","ו")
        i2=0; ok=True
        for ch in letters:
            j=alt.find(ch,i2)
            if j<0: ok=False; break
            i2=j+1
        if ok: return "weak"
    return "reject"

H=json.load(open("hebrew.json",encoding="utf-8"))
forms=collections.Counter()
for v in H.values():
    for w in v["words"]:
        if not w["root"]:
            f=strip(w["hebrew"]).strip('.,:;־׃!?()[]׳״\'" ')
            if f: forms[f]+=1
todo=list(forms)
SYS=("You give the Hebrew triliteral root (shoresh) of a single word from the siddur. "
     "This is liturgical/biblical Hebrew, not modern. Reply with ONLY the root as letters "
     "separated by hyphens, e.g. מ-ל-כ . If the word is a particle, proper name, or has no "
     "root, reply exactly: NONE")
def one(f):
    for _ in range(3):
        try:
            r=requests.post("https://openrouter.ai/api/v1/chat/completions",
              headers={"Authorization":f"Bearer {K}","Content-Type":"application/json"},
              json={"model":MODEL,"temperature":0,"max_tokens":24,
                    "messages":[{"role":"system","content":SYS},{"role":"user","content":f}]},
              timeout=45)
            if r.status_code!=200: time.sleep(1); continue
            j=r.json(); t=j["choices"][0]["message"]["content"].strip()
            u=j.get("usage",{})
            return f,t,u.get("prompt_tokens",0),u.get("completion_tokens",0)
        except Exception: time.sleep(1)
    return f,None,0,0
t0=time.time()
with ThreadPoolExecutor(16) as ex: res=list(ex.map(one,todo))
pt=sum(r[2] for r in res); ct=sum(r[3] for r in res)
out={}; tally=collections.Counter()
for f,t,_,_ in res:
    if not t: tally["error"]+=1; continue
    if t.upper().startswith("NONE"): tally["none"]+=1; out[f]={"root":None,"basis":"none"}; continue
    root=re.sub(r'[^֐-ת-]','',t).strip('-')
    if not root: tally["unparsed"]+=1; continue
    g=grade(f,root); tally[g]+=1
    out[f]={"root":root if g!="reject" else None,"basis":g,"raw":root}
json.dump(out,open("model_roots.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(f"  {len(todo)} forms in {time.time()-t0:.0f}s · {pt:,}+{ct:,} tok · ~${pt/1e6*0.10+ct/1e6*0.40:.4f}")
for k,v in tally.most_common(): print(f"    {k:10} {v:>4}")
cov=sum(forms[f] for f,o in out.items() if o["root"])
print(f"  word instances newly rooted: {cov:,} of 1,065")
