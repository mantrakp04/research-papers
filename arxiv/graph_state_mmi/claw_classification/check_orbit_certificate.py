"""Check finite LC-orbit certificates without performing an orbit search.

Only Python's standard library is required. Run next to orbit_certificate.json.
Each graph is verified reachable using its supplied LC word. The finite set must
contain the representative, be closed under every LC generator, and be claw-free.
Reachability and closure certify that the finite set is exactly the LC orbit.
"""
from pathlib import Path
from itertools import combinations
import json
ROOT=Path(__file__).resolve().parent

def representative(n):
    edges=[(i,i+1) for i in range(n-1)] if n<5 else [(i,(i+1)%5) for i in range(5)]
    if n==6:edges += [(i,5) for i in range(5)]
    g=[[0]*n for _ in range(n)]
    for i,j in edges:g[i][j]=g[j][i]=1
    return tuple(map(tuple,g))

def lc(g,v):
    assert 0<=v<len(g)
    h=[list(row) for row in g]
    neighbors=[i for i in range(len(g)) if g[v][i]]
    for i,j in combinations(neighbors,2):h[i][j]=1-h[i][j];h[j][i]=1-h[j][i]
    return tuple(map(tuple,h))

def decode(rows,n):
    assert len(rows)==n and all(type(x) is int and 0<=x<(1<<n) for x in rows)
    g=tuple(tuple((rows[i]>>j)&1 for j in range(n)) for i in range(n))
    assert all(g[i][i]==0 for i in range(n))
    assert all(g[i][j]==g[j][i] for i in range(n) for j in range(n))
    return g

def no_claw(g):
    for U in combinations(range(len(g)),4):
        if sorted(sum(g[i][j] for j in U) for i in U)==[1,1,1,3]:return False
    return True

def main():
    certificate=json.loads((ROOT/'orbit_certificate.json').read_text())
    assert certificate['format']=='labelled-lc-orbit-v1'
    families=certificate['families'];assert [f['n'] for f in families]==list(range(1,7))
    sizes=[]
    for family in families:
        n=family['n'];base=representative(n);graphs=set()
        for entry in family['graphs']:
            g=decode(entry['adjacency_rows'],n)
            assert g not in graphs;graphs.add(g)
            h=base
            for v in entry['lc_word']:h=lc(h,v)
            assert h==g and no_claw(g)
        assert base in graphs
        assert all(lc(g,v) in graphs for g in graphs for v in range(n))
        sizes.append(len(graphs))
        print(f'{family["representative"]}: {len(graphs)} reachable graphs; closed under every LC; no induced claw')
    assert sizes==[1,1,4,11,132,132]
    print('PASS: all 281 listed graphs form the six exact labelled LC orbits')
if __name__=='__main__':main()
