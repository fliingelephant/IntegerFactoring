#!/usr/bin/env sage-python
"""Exact fitting and held-out checks for a specified fixed-order depth model."""
import json
import signal
import time
from pathlib import Path

signal.alarm(30)
started = time.monotonic()
from sage.all import QQ, ZZ, matrix, vector

folder = Path(__file__).resolve().parent
raw = [json.loads(line) for line in (folder/'reciprocal_trace.jsonl').read_text().splitlines() if line.startswith('{')]
complete = [row for row in raw if row.get('status') == 'complete']
records = []
for target in (1,3,5):
    available = sorted((row for row in complete if row['N']==target),key=lambda row:row['k'])
    for first_k in (4,8,12):
        rows = [row for row in available if row['k']>=first_k]
        sequence = [ZZ(row['signed_convolution']) for row in rows]
        assert [row['k'] for row in rows] == list(range(first_k,first_k+len(rows)))
        hankel = matrix(ZZ,11,11,lambda i,j:sequence[i+j])
        models = []
        for order in range(1,11):
            lhs = matrix(QQ,order,order,lambda i,j:sequence[order+i-j-1])
            rhs = vector(QQ,sequence[order:2*order])
            rank = lhs.rank()
            if lhs.augment(matrix(QQ,order,1,list(rhs))).rank() > rank:
                models.append({'order':order,'fit':'inconsistent'})
                continue
            if rank < order:
                models.append({'order':order,'fit':'underdetermined'})
                continue
            coefficients = lhs.solve_right(rhs)
            prediction = list(sequence[:2*order])
            failure = None
            for i in range(2*order,len(sequence)):
                value = sum(coefficients[j]*prediction[i-j-1] for j in range(order))
                prediction.append(value)
                if value != sequence[i]:
                    failure = {'k':first_k+i,'actual':str(sequence[i]),'prediction':str(value)}
                    break
            models.append({'order':order,'fit':'unique','held_out_failure':failure})
        records.append({'N_residue':target,'first_k':first_k,'last_k':rows[-1]['k'],
                        'hankel_size':11,'hankel_rank':int(hankel.rank()),
                        'hankel_determinant':str(hankel.det()),'models':models})
result = {'family':'route:F31','experiment':'experiment:F293_carry_convolution',
          'status':'exact_finite_recurrence_check','maximum_tested_order':10,
          'elapsed_seconds':time.monotonic()-started,'records':records}
(folder/'recurrence_check.json').write_text(json.dumps(result,indent=2)+'\n')
for row in records:
    print('N',row['N_residue'],'start',row['first_k'],'rank',row['hankel_rank'],
          'order10',row['models'][-1],flush=True)
