#!/usr/bin/env python3
import argparse, csv, hashlib, json, math
from pathlib import Path

N=20000000499999937; P=100000007; Q=199999991; A=2942

def crt(xp,xq): return xp+P*(((xq-xp)*pow(P,-1,Q))%Q)
def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''): h.update(block)
    return h.hexdigest()

parser=argparse.ArgumentParser(); parser.add_argument('--root',required=True); parser.add_argument('--output',required=True); args=parser.parse_args()
root=Path(args.root).resolve(); rows=[]
with (root/'outputs/all_exchange_certificates.csv').open(newline='') as f:
    for raw in csv.DictReader(f):
        r={k:int(v) for k,v in raw.items()}; rows.append(r)
        exponent=(r['base_row_1']+1)+(r['base_row_2']+1)+(A-1)+A
        if r['sign'] != (-1 if exponent%2 else 1): raise SystemExit('sign mismatch')
        if r['formula_p'] != r['sign']*56136614*r['quotient_p']%P: raise SystemExit('p formula mismatch')
        if r['formula_q'] != r['sign']*132391112*r['quotient_q']%Q: raise SystemExit('q formula mismatch')
        if (r['formula_p'],r['formula_q']) != (r['direct_p'],r['direct_q']): raise SystemExit('direct mismatch')
        if r['global_value'] != crt(r['direct_p'],r['direct_q']): raise SystemExit('CRT mismatch')
        if r['gcd_N'] != math.gcd(r['global_value'],N) or r['gcd_N'] not in (P,Q): raise SystemExit('gcd mismatch')
summary=json.loads((root/'outputs/certify_all_summary.json').read_text())
if summary['status']!='pass' or summary['mismatches_certified']!=len(rows) or len(rows)!=2: raise SystemExit('summary mismatch')
manifest={}
for line in (root/'manifests/run_002.outputs.sha256').read_text().splitlines():
    d,name=line.split(maxsplit=1); manifest[name.strip()]=d
for rel in ('outputs/all_exchange_certificates.csv','outputs/certify_all_summary.json'):
    if manifest.get(rel)!=sha(root/rel): raise SystemExit('hash mismatch')
Path(args.output).write_text(json.dumps({'status':'pass','certificates_recomputed':len(rows),'factors':sorted({r['gcd_N'] for r in rows})},indent=2,sort_keys=True)+'\n')

