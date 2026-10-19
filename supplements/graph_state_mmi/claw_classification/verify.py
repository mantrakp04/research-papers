"""Independent matrix/set audit: no imports from proposed proof/search code."""
from collections import deque, Counter
from itertools import product, combinations
from pathlib import Path
import json, hashlib

ROOT = Path(__file__).resolve().parent
OUT = ROOT

def matrix(n,edges):
    m=[[0]*n for _ in range(n)]
    for i,j in edges:m[i][j]=m[j][i]=1
    return tuple(map(tuple,m))

def rep(n):
    if n<5:return matrix(n,[(i,i+1) for i in range(n-1)])
    edges=[(i,(i+1)%5) for i in range(5)]
    if n==6:edges += [(i,5) for i in range(5)]
    return matrix(n,edges)

def complement(m,v):
    return tuple(tuple(0 if i==j else m[i][j]^(m[i][v]*m[j][v]) for j in range(len(m))) for i in range(len(m)))

def transform(m,seq):
    for v in seq:
        assert 0<=v<len(m)
        m=complement(m,v)
    return m

def extend(m,mask):
    n=len(m)
    return tuple(tuple(row)+((mask>>i)&1,) for i,row in enumerate(m))+(tuple((mask>>i)&1 for i in range(n))+(0,),)

def relabel(m,p):
    n=len(m);ret=[[0]*n for _ in range(n)]
    assert sorted(p)==list(range(n))
    for i in range(n):
        for j in range(n):ret[p[i]][p[j]]=m[i][j]
    return tuple(map(tuple,ret))

def claws(m):
    ret=[]
    for four in combinations(range(len(m)),4):
        deg=[sum(m[i][j] for j in four) for i in four]
        if sorted(deg)==[1,1,1,3]:ret.append(tuple(four))
    return ret

def orbit(m):
    seen={m};q=deque([m])
    while q:
        m=q.popleft()
        for v in range(len(m)):
            nxt=complement(m,v)
            if nxt not in seen:seen.add(nxt);q.append(nxt)
    return seen

def rank(m,A):
    n=len(m);B=set(range(n))-set(A)
    # Independent set-based Gaussian elimination (symmetric difference).
    basis={}
    for i in A:
        row={j for j in B if m[i][j]}
        while row:
            p=min(row)
            if p not in basis:basis[p]=row;break
            row=row^basis[p]
    return len(basis)

def entropy_profile(m):
    n=len(m);S={mask:rank(m,[i for i in range(n) if mask>>i&1]) for mask in range(1<<n)}
    hist=Counter();hist_nonempty=Counter();examples={}
    for assign in product(range(4),repeat=n):
        parts=[sum(1<<i for i,x in enumerate(assign) if x==j) for j in range(4)]
        a,b,c,d=parts
        I=S[a]+S[b]+S[c]-S[a|b]-S[a|c]-S[b|c]+S[a|b|c]
        hist[I]+=1
        if all(parts):hist_nonempty[I]+=1
        examples.setdefault(I,parts)
    return S,dict(sorted(hist.items())),dict(sorted(hist_nonempty.items())),examples

certdata=(ROOT/'extension_certificate.json').read_bytes()
cert=json.loads(certdata)
seen=set();counts=Counter();lc_lengths=Counter()
for row in cert:
    n=row['n'];mask=row['attachment'];key=(n,mask)
    assert key not in seen;seen.add(key)
    assert 2<=n<=7 and 1<=mask<(1<<(n-1))
    m=transform(extend(rep(n-1),mask),row['lc_sequence'])
    assert all(m[i][j]==m[j][i] and m[i][i]==0 for i in range(n) for j in range(n))
    if row['outcome']=='claw':
        center,*leaf=row['claw']
        assert len(set([center]+leaf))==4
        assert all(m[center][i] for i in leaf)
        assert all(m[i][j]==0 for i,j in combinations(leaf,2))
        assert claws(m)
    else:
        assert row['outcome']=='next_representative' and n<7
        assert m==relabel(rep(n),row['permutation'])
    counts[(n,row['outcome'])]+=1
    lc_lengths[len(row['lc_sequence'])]+=1
assert seen=={(n,mask) for n in range(2,8) for mask in range(1,1<<(n-1))}
print('CERTIFICATE: all 120 rows valid, all attachment masks exactly covered')
print('counts:',sorted(counts.items()))
print('LC lengths:',sorted(lc_lengths.items()))
report={'certificate_sha256':hashlib.sha256(certdata).hexdigest(),'certificate_cases':len(cert),'extension_counts':[{'n':n,'outcome':o,'count':k} for (n,o),k in sorted(counts.items())],'profiles':[]}
for n in range(1,7):
    m=rep(n);orb=orbit(m)
    assert all(not claws(h) for h in orb)
    s,h,h4,ex=entropy_profile(m)
    assert max(h)<=0
    # Independently test entire labelled LC orbit retains all subset entropies.
    assert all(all(rank(g,[i for i in range(n) if mask>>i&1])==s[mask] for mask in s) for g in orb)
    row={'n':n,'labelled_lc_orbit_size':len(orb),'i3_all_labelled_four_partitions':h,'i3_all_nonempty_labelled_four_partitions':h4,'subset_entropies':s}
    report['profiles'].append(row)
    print('REP',n,'orbit',len(orb),'I3 hist incl empties',h,'nonempty',h4)
# Counterexample to sufficiency and witness sequence on P5.
p5=matrix(5,[(0,1),(1,2),(2,3),(3,4)])
p5hist=entropy_profile(p5)[1]
assert max(p5hist)<=0
q=deque([(p5,[])]);vis={p5};found=None
while q:
    m,seq=q.popleft()
    if claws(m):found={'lc_sequence':seq,'claw_vertex_set':claws(m)[0]};break
    for v in range(5):
        g=complement(m,v)
        if g not in vis:vis.add(g);q.append((g,seq+[v]))
assert found
report['p5']={'i3_histogram':p5hist,**found}
print('P5 MMI / CLAW WITNESS',report['p5'])
(OUT/'audit_result.json').write_text(json.dumps(report,indent=2)+'\n')
