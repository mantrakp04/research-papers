"""Independent path graph-state MMI audit. Standard library only; no claimant imports."""
import itertools, json, random, collections, time
from pathlib import Path
OUT=Path(__file__).resolve().parent
SUBSETS=(frozenset([0]),frozenset([1]),frozenset([2]),frozenset([0,1,2]),frozenset([0,1]),frozenset([0,2]),frozenset([1,2]))
SIGNS=(1,1,1,1,-1,-1,-1)

def rank_gf2(rows):
    pivots={}
    for row in rows:
        while row:
            pivot=row.bit_length()-1
            if pivot not in pivots:
                pivots[pivot]=row
                break
            row ^= pivots[pivot]
    return len(pivots)

def cutrank(n,mask):
    # Matrix has rows indexed by vertices in cut, columns in complement.
    # Keep full vertex coordinates as columns; all cut-side columns are zero.
    outside=((1<<n)-1)^mask
    rows=[]
    for j in range(n):
        if mask>>j&1:
            adjacency=(1<<(j-1) if j else 0)|(1<<(j+1) if j+1<n else 0)
            rows.append(adjacency & outside)
    return rank_gf2(rows)

def cut_matching_dp(n,mask):
    # True optimum via dynamic programming, independent of greedy automaton.
    prev2=prev1=0
    for j in range(1,n):
        crossing=((mask>>(j-1))^(mask>>j))&1
        best=max(prev1,prev2+crossing)
        prev2,prev1=prev1,best
    return prev1

def calc_automaton(colors):
    chosen=[False]*7
    scores=[0]*7
    for left,right in zip(colors,colors[1:]):
        chosen=[((left in s)!=(right in s)) and not prior for s,prior in zip(SUBSETS,chosen)]
        scores=[x+int(y) for x,y in zip(scores,chosen)]
    return scores

def own_states():
    states={(c,(False,)*7) for c in range(4)}
    queue=collections.deque(states)
    edges=set()
    while queue:
        u=queue.popleft()
        for new in range(4):
            chosen=tuple(((u[0] in s)!=(new in s)) and not p for s,p in zip(SUBSETS,u[1]))
            v=(new,chosen)
            weight=sum(sign*x for sign,x in zip(SIGNS,chosen))
            edges.add((u,v,weight))
            if v not in states:
                states.add(v);queue.append(v)
    return states,edges

def mask_of(bits):return sum(int(b)<<k for k,b in enumerate(bits))
def certificate_audit():
    data=json.loads((OUT/'path_certificate.json').read_text())
    assert data['cuts']==[1,2,4,7,3,5,6]
    assert data['coefficients']==list(SIGNS)
    raw=data['potentials'];assert len(raw)==len(set((a,q) for a,q,p in raw))
    potentials={(a,tuple(bool(q>>k&1) for k in range(7))):p for a,q,p in raw}
    states,edges=own_states()
    assert set(potentials)==states
    recorded_edges=set(((u[0],tuple(bool(u[1]>>k&1) for k in range(7))),(v[0],tuple(bool(v[1]>>k&1) for k in range(7))),w) for u,v,w in data['edges'])
    assert len(data['edges'])==len(recorded_edges)
    assert edges==recorded_edges
    assert all(potentials[c,(False,)*7]==0 for c in range(4))
    assert all(p<=0 and isinstance(p,int) for p in potentials.values())
    slack=collections.Counter()
    for u,v,w in edges:
        d=potentials[v]-potentials[u]-w
        assert d>=0,(u,v,w)
        slack[d]+=1
    # This simplification is a discovered check, not an assumption.
    assert all(p==min(0,sum(s*b for s,b in zip(SIGNS,q))) for (a,q),p in potentials.items())
    return {'reachable_states':len(states),'edges':len(edges),'potentials':dict(collections.Counter(potentials.values())),'edge_slacks':dict(slack)}

def exhaustive():
    results=[]
    for n in range(1,11):
        ent=[cutrank(n,mask) for mask in range(1<<n)]
        assert all(ent[m]==cut_matching_dp(n,m) for m in range(1<<n))
        dist=collections.Counter()
        for colors in itertools.product(range(4),repeat=n):
            group=[0,0,0,0]
            for j,c in enumerate(colors):group[c]|=1<<j
            a,b,c,d=group
            scores=[ent[m] for m in (a,b,c,a|b|c,a|b,a|c,b|c)]
            auto=calc_automaton(colors)
            assert scores==auto,(colors,scores,auto)
            i3=sum(s*x for s,x in zip(SIGNS,scores))
            assert i3<=0,(n,colors,i3)
            dist[i3]+=1
        row={'n':n,'four_colorings':4**n,'min_I3':min(dist),'max_I3':max(dist),'distribution':dict(sorted(dist.items()))}
        print(row,flush=True);results.append(row)
    return results

def random_audit():
    rng=random.Random(74216301);results=[]
    for n,trials in [(11,500),(20,500),(50,500),(100,500),(500,100),(1000,100)]:
        worst=-n;best=n
        for _ in range(trials):
            colors=[rng.randrange(4) for _ in range(n)]
            masks=[sum(1<<j for j,c in enumerate(colors) if c in subset) for subset in SUBSETS]
            ranks=[cutrank(n,m) for m in masks]
            assert ranks==calc_automaton(colors)
            assert ranks==[cut_matching_dp(n,m) for m in masks]
            i3=sum(s*r for s,r in zip(SIGNS,ranks));assert i3<=0
            worst=max(worst,i3);best=min(best,i3)
        row={'n':n,'trials':trials,'min_I3':best,'max_I3':worst};print(row,flush=True);results.append(row)
    return results

if __name__=='__main__':
    t=time.monotonic()
    cert=certificate_audit();print('CERTIFICATE',cert,flush=True)
    exhaustive_results=exhaustive()
    random_results=random_audit()
    result={'certificate':cert,'exhaustive':exhaustive_results,'random':random_results,'seconds':time.monotonic()-t}
    (OUT/'independent_audit_results.json').write_text(json.dumps(result,indent=2))
    print('ALL INDEPENDENT CHECKS PASSED',result['seconds'],flush=True)
