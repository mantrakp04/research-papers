#!/usr/bin/env python3
"""Standalone exact verification. Requires only Python standard library.
Run from any directory; the JSON certificate is adjacent to this script.
The mathematical reduction and interpretation are in the corresponding manuscript
(latex/rank_one_four_matrix_note/main.tex in the combined bundle).
"""
from collections import Counter
from itertools import combinations, permutations, product
from pathlib import Path
import json

E=list(combinations(range(4),2));EI={e:i for i,e in enumerate(E)}
K=((3,0,0,0),(3,1,0,0),(3,2,1,0),(3,3,3,3))
P=Counter()
for word in product(range(4),repeat=4):
    edge_exponents=[0]*6
    for i,j in zip(word,word[1:]):
        if i!=j:edge_exponents[EI[tuple(sorted((i,j)))]]+=1
    vertex_exponents=tuple(word.count(i) for i in range(4))
    P[tuple(edge_exponents),vertex_exponents]+=24
    if len(set(word))==4:P[tuple(edge_exponents),vertex_exponents]-=256
edge_perms=[]
for p in permutations(range(4)):
    edge_perms.append(tuple(EI[tuple(sorted((p[i],p[j])))] for i,j in E))
def representative(k):
    return min(tuple(k[i] for i in p) for p in edge_perms)
reps={representative(k) for k in product(range(4),repeat=6)}
assert len(reps)==276
cert_list=json.loads((Path(__file__).parent/'rankone_n4_exact_scales.json').read_text())
cert={tuple(x['bernstein_index']):x for x in cert_list}
assert len(cert)==len(cert_list)==240
nonnegative=0;amgm=0;smallest_gap=None
for k in sorted(reps):
    C=Counter()
    for (e,a),c in P.items():
        for j in range(6):c*=K[k[j]][e[j]]
        C[a]+=c
    negative=[a for a,c in C.items() if c<0]
    if not negative:
        assert k not in cert
        nonnegative+=1
        continue
    assert negative==[(1,1,1,1)]
    s=cert[k]['scales']
    assert len(s)==4 and all(type(x) is int and x>0 for x in s)
    D={}
    for a,c in C.items():
        if c>0:
            for j in range(4):c*=s[j]**a[j]
            D[a]=c
    target=-C[(1,1,1,1)]
    for x in s:target*=x
    g=[sum(c*(a[i]-1) for a,c in D.items()) for i in range(4)]
    assert sum(g)==0
    R=-min(g)
    weights={a:4*c for a,c in D.items()}
    for i in range(4):
        a=tuple(4 if i==j else 0 for j in range(4))
        assert a in weights
        removal=g[i]+R
        assert 0<=removal<=weights[a]
        weights[a]-=removal
    assert all(c>=0 for c in weights.values())
    assert all(sum(c*(a[i]-1) for a,c in weights.items())==0 for i in range(4))
    gap=sum(weights.values())-4*target
    assert gap>=0
    assert str(gap)==cert[k]['gap']
    smallest_gap=gap if smallest_gap is None else min(smallest_gap,gap)
    amgm+=1
assert (nonnegative,amgm)==(36,240)
print('PASS: 4,096 Bernstein coefficients covered by 276 vertex-permutation orbits')
print('PASS: 36 coefficientwise nonnegative orbits; 240 exact rational AM-GM certificates')
print('PASS: all arithmetic uses Python integers; no numeric optimization or tolerance')
print('Scope: four arbitrary rank-one PSD matrices; product length four; every UI norm')
print('This does NOT establish the full Duchi conjecture or establish novelty')
