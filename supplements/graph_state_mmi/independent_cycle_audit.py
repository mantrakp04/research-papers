"""Cycle audit: fresh direct ranks, cyclic cut-run formula, and four-edge-type proof."""
import itertools, json, random, collections, time
from pathlib import Path
OUT=Path(__file__).resolve().parent
CUTS=(frozenset([0]),frozenset([1]),frozenset([2]),frozenset([3]),frozenset([0,1]),frozenset([0,2]),frozenset([0,3]))
SIGNS=(1,1,1,1,-1,-1,-1)
def gf2rank(rows):
    basis={}
    for r in rows:
        while r:
            k=r.bit_length()-1
            if k not in basis:basis[k]=r;break
            r^=basis[k]
    return len(basis)
def rank(n,subset):
    mask=sum(1<<j for j in subset)
    out=((1<<n)-1)^mask
    return gf2rank([((1<<((j-1)%n))|(1<<((j+1)%n)))&out for j in subset])
def circular_runs(values):
    if len(set(values))==1:return [(values[0],len(values))]
    start=next(j for j in range(len(values)) if values[j-1]!=values[j])
    runs=[]
    for j in range(len(values)):
        value=values[(start+j)%len(values)]
        if runs and runs[-1][0]==value:runs[-1]=(value,runs[-1][1]+1)
        else:runs.append((value,1))
    return runs

def periodic_scores(colors):
    n=len(colors)
    bits=[False]*7
    for j in range(n):
        left,right=colors[j],colors[(j+1)%n]
        bits=[((left in s)!=(right in s)) and not b for s,b in zip(CUTS,bits)]
    start=tuple(bits);scores=[0]*7
    for j in range(n):
        left,right=colors[j],colors[(j+1)%n]
        bits=[((left in s)!=(right in s)) and not b for s,b in zip(CUTS,bits)]
        scores=[a+b for a,b in zip(scores,bits)]
    assert tuple(bits)==start
    return scores

def check(colors,entropy=None):
    n=len(colors)
    masks=[sum(1<<j for j,c in enumerate(colors) if c in cut) for cut in CUTS]
    ent=[entropy[m] if entropy is not None else rank(n,[j for j in range(n) if m>>j&1]) for m in masks]
    i3=sum(s*e for s,e in zip(SIGNS,ent))
    assert i3<=0,(colors,ent,i3)
    full=[]
    for k,cut in enumerate(CUTS):
        cross=[(colors[j] in cut)!=(colors[(j+1)%n] in cut) for j in range(n)]
        if all(cross):
            assert n%2==0
            expected=n//2-1
            full.append(k)
        else:
            expected=sum((length+1)//2 for value,length in circular_runs(cross) if value)
        assert ent[k]==expected,(colors,k,ent[k],expected)
    periodic=periodic_scores(colors)
    assert all(ent[k]==periodic[k]-(k in full) for k in range(7))
    assert sum(s*e for s,e in zip(SIGNS,periodic))<=0
    category='missing_color'
    if len(set(colors))==4:
        assert len(full)<=1
        if not full:category='no_full_cut'
        elif full[0]<4:category='full_singleton';assert i3<=-1
        else:
            category='full_pair'
            edge_types=[tuple(sorted((colors[j],colors[(j+1)%n]))) for j in range(n)]
            runs=circular_runs(edge_types)
            odd=sum(length%2 for _,length in runs)
            assert odd>=2 and odd%2==0
            assert i3==1-odd//2,(colors,i3,odd)
            assert sum(ent[:4])==n
    else:assert i3==0
    return i3,category

def main():
    start=time.monotonic();rows=[]
    for n in range(3,11):
        ent=[rank(n,[j for j in range(n) if m>>j&1]) for m in range(1<<n)]
        dist=collections.Counter();cats=collections.Counter()
        for colors in itertools.product(range(4),repeat=n):
            score,cat=check(colors,ent);dist[score]+=1;cats[cat]+=1
        row={'n':n,'colorings':4**n,'distribution':dict(sorted(dist.items())),'categories':dict(cats)}
        rows.append(row);print(row,flush=True)
    rng=random.Random(817355);random_results=[]
    for n,count in [(11,100),(20,100),(50,100),(100,100),(500,100),(1000,100)]:
        for _ in range(count):check([rng.randrange(4) for j in range(n)])
        # Deliberately sample hard full-pair/full-singleton cases on even cycles.
        if n%2==0:
            for _ in range(count):
                check([rng.choice([0,1]) if j%2==0 else rng.choice([2,3]) for j in range(n)])
                check([0 if j%2==0 else rng.choice([1,2,3]) for j in range(n)])
        row={'n':n,'unrestricted':count,'full_pair_and_singleton_each':count if n%2==0 else 0};random_results.append(row);print(row,flush=True)
    data={'exhaustive':rows,'random':random_results,'seconds':time.monotonic()-start}
    (OUT/'independent_cycle_results.json').write_text(json.dumps(data,indent=2))
    print('CYCLE CHECKS PASSED',data['seconds'],flush=True)
if __name__=='__main__':main()
