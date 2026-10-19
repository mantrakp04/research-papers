"""Independent exact finite check using shifted cosine coefficients and rational Sturm.
This does not prove the all-n uniform analytic bounds.
"""
from fractions import Fraction as F
from math import factorial, comb
import json, time
from pathlib import Path
import sympy as s
x=s.Symbol('x')

def shifted_coefficients(n):
    # [z^n](2 asin(sqrt(z)/2))^(2k) via elementary symmetric functions.
    es=[1]+[0]*(n-1)
    for i in range(1,n):
        for j in range(i,0,-1):es[j]+=i*i*es[j-1]
    coeff=[]
    for k in range(1,n+1):
        B=F(s.bernoulli(2*k))
        coeff.append(F(n*(-1)**(k+1)*2**(2*k-1)*(4**k-1)*es[n-k],k*factorial(2*n))*B)
    return coeff

def trace(n,N,c):
    xx=F(2*N+1,2)
    ans=sum((ck*(xx**(2*k)-F(1,2)**(2*k)) for k,ck in enumerate(c,1)),F(0))
    assert ans.denominator==1
    return ans.numerator

def gamma_from_h(h):
    d=len(h)-1; rem=list(h); g=[]
    for j in range(d//2+1):
        a=rem[j];g.append(a)
        for k in range(j,d-j+1):rem[k]-=a*comb(d-2*j,k-j)
    assert all(a==0 for a in rem)
    return g

def sign(a):return (a>0)-(a<0)
def variations(signs):
    signs=[a for a in signs if a]
    return sum(a!=b for a,b in zip(signs,signs[1:]))
rows=[]
comparison=Path(__file__).with_name('optional_reference_hstar.json')
existing=json.loads(comparison.read_text()) if comparison.exists() else None
for n in range(2,41):
    start=time.time();c=shifted_coefficients(n)
    vals=[trace(n,m+1,c) for m in range(2*n+1)]
    h=[sum((-1)**j*comb(2*n+1,j)*vals[k-j] for j in range(k+1)) for k in range(2*n+1)]
    assert h[-2:]==[0,0];h=h[:-2]
    assert h[0]==h[-1]==1 and h==h[::-1]
    if existing is not None: assert h==existing[n-2]['h']
    g=gamma_from_h(h)
    p=s.Poly.from_list(g[::-1],x,domain=s.QQ)
    seq=s.polys.polytools.sturm(p)
    signs_inf=[sign(int(s.sign(p.LC())))*(-1)**p.degree() for p in seq]
    signs_zero=[int(s.sign(p.eval(0))) for p in seq]
    vinf=variations(signs_inf);vzero=variations(signs_zero)
    gcd=s.gcd(p,p.diff()).degree()
    assert vinf-vzero==p.degree()
    assert gcd==0
    if n==2:assert h==[1,2,1]
    else:assert p.degree()==n-1
    row=dict(n=n,h_degree=len(h)-1,gamma_degree=p.degree(),sturm_degrees=[q.degree() for q in seq],sturm_signs_minus_infinity=signs_inf,sturm_signs_zero=signs_zero,Vminusinf=vinf,Vzero=vzero,negative_distinct_gamma_roots=vinf-vzero,gcd_degree=gcd)
    rows.append(row)
    with open(Path(__file__).with_name('independent_sturm_results.json'),'w') as f:json.dump(rows,f,indent=2)
    print(n,vinf,vzero,p.degree(),'seconds',round(time.time()-start,3),flush=True)
print('PASS: n=2 double root -1; n=3..40 have 2n-2 distinct negative roots.')
