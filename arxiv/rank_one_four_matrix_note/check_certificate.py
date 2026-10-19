"""Independent exhaustive standard-library audit of supplied scale certificate.
No author checker, numerical optimizer, NumPy array, or floating point is used.
"""
import collections
import fractions
import hashlib
import itertools
import json
import math
import sys
from pathlib import Path

F = fractions.Fraction
if not __debug__:
    raise RuntimeError('Run without Python -O: this checker uses assertions.')
CERT_PATH = Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('rankone_n4_exact_scales.json')
raw_bytes = CERT_PATH.read_bytes()
records = json.loads(raw_bytes)
vertices = tuple(range(4))
edges = tuple(itertools.combinations(vertices, 2))
edge_id = {e: i for i, e in enumerate(edges)}
indices = list(itertools.product(range(4), repeat=6))
perms = list(itertools.permutations(vertices))
center = (1, 1, 1, 1)

# Derive univariate power-to-Bernstein conversion by exact Gaussian elimination
# of Bernstein polynomial expansions, instead of using the author's K matrix.
B = [[F(0) for _ in range(4)] for _ in range(4)]
for k in range(4):
    for j in range(4-k):
        B[k+j][k] = F(math.comb(3,k)*math.comb(3-k,j)*(-1)**j)
aug = [row + [F(int(i==j)) for j in range(4)] for i,row in enumerate(B)]
for i in range(4):
    pivot=aug[i][i]
    aug[i] = [v/pivot for v in aug[i]]
    for j in range(4):
        if i != j:
            a=aug[j][i]
            aug[j]=[u-a*v for u,v in zip(aug[j],aug[i])]
M=[row[4:] for row in aug]
K=[[int(v*3) for v in row] for row in M]
assert all(F(K[i][j],3)==M[i][j] for i in range(4) for j in range(4))

# Construct expectation difference at original probabilities, using separate
# with/without replacement loops, then scale by 256*24*3**6.
powers = collections.defaultdict(F)
for word in itertools.product(vertices, repeat=4):
    counts=tuple(word.count(i) for i in vertices)
    walk=[0]*6
    for i,j in zip(word[:-1],word[1:]):
        if i != j:
            walk[edge_id[tuple(sorted([i,j]))]]+=1
    powers[(tuple(walk), counts)] += F(1,256)
for word in itertools.permutations(vertices):
    walk=[0]*6
    for i,j in zip(word[:-1],word[1:]):
        walk[edge_id[tuple(sorted([i,j]))]]+=1
    powers[(tuple(walk), center)] -= F(1,24)
powers={key:int(value*256*24) for key,value in powers.items() if value}
assert all(sum(alpha)==4 and sum(walk)<=3 for walk,alpha in powers)
coeffs={k:collections.Counter() for k in indices}
for (walk,alpha),value in powers.items():
    for k in itertools.product(*(range(a,4) for a in walk)):
        factor=math.prod(K[ki][ai] for ki,ai in zip(k,walk))
        coeffs[k][alpha]+=value*factor
coeffs={k:{a:c for a,c in v.items() if c} for k,v in coeffs.items()}

# Relabel an edge coloring and a lambda monomial in the same direction.
def relabel_index(k,p):
    target=[None]*6
    for old,(i,j) in enumerate(edges):
        target[edge_id[tuple(sorted([p[i],p[j]]))]]=k[old]
    return tuple(target)
def relabel_alpha(a,p):
    result=[None]*4
    for old,new in enumerate(p): result[new]=a[old]
    return tuple(result)

orbits={}
unseen=set(indices)
while unseen:
    rep=min(unseen)
    orbit={relabel_index(rep,p) for p in perms}
    orbits[rep]=orbit
    for p in perms:
        target=relabel_index(rep,p)
        assert {relabel_alpha(a,p):c for a,c in coeffs[rep].items()}==coeffs[target], ('symmetry',rep,p)
    unseen-=orbit
assert sum(map(len,orbits.values()))==4096
supplied={tuple(r['bernstein_index']):r for r in records}
assert len(supplied)==len(records), 'duplicate certificate rows'
required={k for k in orbits if any(v<0 for v in coeffs[k].values())}
assert set(supplied)==required, ('missing/extraneous',required-set(supplied),set(supplied)-required)

margins=[]
for k in required:
    c=coeffs[k]
    assert {a for a,v in c.items() if v<0}=={center}
    s=supplied[k]['scales']
    assert len(s)==4 and all(isinstance(v,int) and v>0 for v in s)
    # Independent reconstruction of the balancing allocation. These quantities
    # are integers, proving the weighted AM-GM certificate without tolerance.
    positive={a:v*math.prod(t**power for t,power in zip(s,a)) for a,v in c.items() if v>0}
    target=-c[center]*math.prod(s)
    gradient=[sum(v*(a[i]-1) for a,v in positive.items()) for i in vertices]
    assert sum(gradient)==0
    shift=-min(gradient)
    allocated={a:4*v for a,v in positive.items()}
    for i in vertices:
        pure=tuple(4 if j==i else 0 for j in vertices)
        allocated[pure]=allocated.get(pure,0)-gradient[i]-shift
    assert all(0<=v<=4*positive.get(a,0) for a,v in allocated.items()), ('resource',k)
    mass=sum(allocated.values())
    assert all(sum(a[i]*v for a,v in allocated.items())==mass for i in vertices), ('barycenter',k)
    gap=mass-4*target
    assert gap>=0, ('deficit',k)
    assert str(gap)==supplied[k]['gap'], ('recorded gap',k)
    margins.append((F(gap,4*target),k))

summary={
  'certificate_sha256':hashlib.sha256(raw_bytes).hexdigest(),
  'power_monomials':len(powers),
  'bernstein_indices':len(indices),
  'permutation_orbits':len(orbits),
  'coefficientwise_nonnegative_orbits':len(orbits)-len(required),
  'weighted_amgm_orbits':len(required),
  'coefficientwise_nonnegative_indices':sum(len(orbits[k]) for k in orbits if k not in required),
  'weighted_amgm_indices':sum(len(orbits[k]) for k in required),
  'minimum_relative_margin':str(min(margins)[0]),
  'zero_margin_orbits':[k for m,k in margins if m==0],
  'minimum_positive_relative_margin':str(min(m for m,k in margins if m>0)),
  'derived_scaled_bernstein_conversion':K,
  'status':'PASS: exact exhaustive coefficients, symmetry, orbit coverage, resource bounds, balance, and AM-GM gaps'
}
print(json.dumps(summary,indent=2))
Path(__file__).with_name('exact_audit_result.json').write_text(json.dumps(summary,indent=2)+'\n')
