from fractions import Fraction as Q
from math import comb, factorial
from itertools import product
import json, time
from pathlib import Path

# Direct matrix multiplication only. No determinant or Newton identities.
def matrix_trace(n,N):
    M=[[N-max(a,b) for b in range(N)] for a in range(N)]
    A=[[int(a==b) for b in range(N)] for a in range(N)]
    for _ in range(n):
        A=[[sum(A[a][k]*M[k][b] for k in range(N)) for b in range(N)] for a in range(N)]
    return sum(A[a][a] for a in range(N))

def values(n,upto):
    C=[matrix_trace(n,m+1) for m in range(upto+1)]
    E=[sum((m-k+1)*C[k] for k in range(m+1)) for m in range(upto+1)]
    return C,E

# Direct coefficient extraction from Lagrange basis, independent of Newton interpolation.
def lagrange_linear(v):
    d=len(v)-1
    return -v[0]*sum((Q(1,j) for j in range(1,d+1)),Q(0))+sum((Q((-1)**(j-1)*comb(d,j)*v[j],j) for j in range(1,d+1)),Q(0))

def lagrange_polynomial(v):
    d=len(v)-1
    total=[Q(0) for _ in range(d+1)]
    for j,y in enumerate(v):
        a=[Q(1)]; denom=1
        for k in range(d+1):
            if j==k: continue
            b=[Q(0) for _ in range(len(a)+1)]
            for i,z in enumerate(a): b[i]-=k*z; b[i+1]+=z
            a=b; denom*=j-k
        for i,z in enumerate(a): total[i]+=Q(y,denom)*z
    return total

def evaluate(a,x):
    y=Q(0)
    for z in reversed(a): y=y*x+z
    return y

# Enumerate every coordinate tuple in the FULL face lattice, including bottom/top.
def brute_full(n,m):
    count=0
    for z in product(range(m+1),repeat=2*n+2):
        bottom,top=z[0],z[-1]; a=z[1:1+n]; b=z[1+n:-1]
        if all(bottom<=a[i]<=b[i]<=top and a[(i+1)%n]<=b[i] for i in range(n)):
            count+=1
    return count

report={"method":"direct integer transfer-matrix multiplication and rational Lagrange interpolation", "checks":[]}
for n,m in [(3,0),(3,1),(3,2),(3,3),(4,1),(4,2),(5,1)]:
    brute=brute_full(n,m); direct=values(n,m)[1][m]
    assert brute==direct
    report['checks'].append(dict(n=n,m=m,brute=brute,formula=direct))
    print('brute',n,m,brute,flush=True)

for n in range(3,14):
    d=2*n+2
    C,E=values(n,d+3)
    coef=lagrange_polynomial(E[:d+1])
    linear=lagrange_linear(E[:d+1])
    assert linear==coef[1]
    assert all(evaluate(coef,m)==E[m] for m in range(d+1,d+4))
    assert coef[0]==1 and coef[-1]>0
    # Ehrhart reciprocity gives zeros at -1,-2,-3,-4 for this rank-3 poset;
    # symmetry E(-5-m)=E(m), since d is even and the poset is graded.
    assert all(evaluate(coef,-m)==0 for m in range(1,5))
    assert all(evaluate(coef,-5-m)==E[m] for m in range(d+1))
    negatives=[i for i,c in enumerate(coef) if c<0]
    r=dict(n=n,degree=d,linear=str(linear),negative_indices=negatives,coefficients=list(map(str,coef)),crown_values=C,values=E,leading_times_factorial=str(coef[-1]*factorial(d)))
    report.setdefault('polynomials',[]).append(r)
    print('n',n,'degree',d,'linear',linear,'negative_indices',negatives,flush=True)
    if n==7:
        # Omega(t)=E(t-1). Coefficient at t is E'(-1).
        order_linear=sum((i*coef[i]*(-1)**(i-1) for i in range(1,len(coef))),Q(0))
        assert order_linear==Q(-3,1430)
        report['paper_n7_order_linear']=str(order_linear)
        print('paper n7 order linear',order_linear,flush=True)

with open(Path(__file__).resolve().parent/'independent_results.json','w') as f:json.dump(report,f,indent=2)
print('ALL ASSERTIONS PASSED',flush=True)
