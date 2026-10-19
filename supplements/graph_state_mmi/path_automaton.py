from collections import deque
from pathlib import Path
from itertools import product
# Colors 0,1,2,3 label A,B,C,D. These seven cuts specify I_3(A:B:C).
CUTS=(1,2,4,7,3,5,6)
COEFF=(1,1,1,1,-1,-1,-1)
def crossing(a,b):
    return sum((((mask>>a)&1)^((mask>>b)&1))<<i for i,mask in enumerate(CUTS))
def weight(mask): return sum(c for i,c in enumerate(COEFF) if (mask>>i)&1)
def transition(state,b):
    a,q=state
    r=crossing(a,b)&~q
    return (b,r),weight(r)
initial=[(a,0) for a in range(4)]
seen=set(initial);queue=deque(initial);edges=[]
while queue:
    u=queue.popleft()
    for b in range(4):
        v,w=transition(u,b);edges.append((u,v,w))
        if v not in seen:seen.add(v);queue.append(v)
print('reachable states',len(seen),'edges',len(edges))
# Longest-path Bellman-Ford, initialize only zero-edge paths.
d={u:float('-inf') for u in seen};d.update({u:0 for u in initial})
witness={u:(u[0],) for u in initial}
for it in range(len(seen)):
    changed=False
    for u,v,w in edges:
        if d[u]+w>d[v]:
            d[v]=d[u]+w;witness[v]=witness[u]+(v[0],);changed=True
    print('iteration',it,'max',max(d.values()),'changes',changed)
    if not changed:break
else: print('Positive cycle or need extra iteration')
viol=[(v,d[v],witness[v]) for v in seen if d[v]>0]
print('violations',viol[:3]);print('potential distribution',{i:list(d.values()).count(i) for i in set(d.values())})
# Independently verify finite potential certificate: p(start)>=0;
# p(v)>=p(u)+w; p(v)<=0 for all states. Then telescoping proves I_3<=0.
assert all(d[u]>=0 for u in initial)
assert all(d[v]>=d[u]+w for u,v,w in edges)
assert all(d[v]<=0 for v in seen)
import json
from pathlib import Path
with Path(__file__).with_name('path_certificate.json').open('w') as f:
    json.dump({'cuts':CUTS,'coefficients':COEFF,'potentials':[[a,q,d[a,q]] for a,q in sorted(seen)],'edges':[[u,v,w] for u,v,w in edges]},f,indent=2)
print('CERTIFICATE CHECKED')
