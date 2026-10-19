"""Exact standard-library finite root and rational-bound verification.
Run with Python 3 (without -O); adjacent finite_sign_certificates.json required.
No floats, SymPy, network, or stored h* coefficients are used.
See the corresponding manuscript for the symbolic analytic proof
(latex/crown_real_rootedness/main.tex in the combined bundle).
"""
from fractions import Fraction as F
from math import comb,factorial
from pathlib import Path
import json

def trace(n,N):
    e=[comb(N+j,2*j) for j in range(n+1)]
    p=[N]
    for r in range(1,n+1):
        p.append(sum((-1)**(j-1)*e[j]*p[r-j] for j in range(1,r))
                 +(-1)**(r-1)*r*e[r])
    return p[n]

def hstar(n):
    L=[trace(n,m+1) for m in range(2*n+1)]
    h=[sum((-1)**j*comb(2*n+1,j)*L[k-j] for j in range(k+1))
       for k in range(2*n+1)]
    assert h[-2:]==[0,0]
    h=h[:-2]
    assert h==h[::-1] and h[0]==1 and h[-1]==1
    return h

def gamma(h):
    d=len(h)-1;remainder=h[:];g=[]
    for j in range(d//2+1):
        value=remainder[j];g.append(value)
        for k in range(j,d-j+1):remainder[k]-=value*comb(d-2*j,k-j)
    assert not any(remainder)
    return g

def sign_at(a,p,D):
    value=a[-1];power=D
    for coefficient in a[-2::-1]:
        value=value*p+coefficient*power;power*=D
    return (value>0)-(value<0)

assert hstar(2)==[1,2,1]
certificates=json.loads(Path(__file__).with_name('finite_sign_certificates.json').read_text())
assert [c['n'] for c in certificates]==list(range(3,40))
for c in certificates:
    n=c['n'];g=gamma(hstar(n));assert g==c['gamma']
    assert len(g)==n and g[-1]!=0
    D=int(c['denominator']);assert D>0
    points=list(map(int,c['boundary_numerators']))
    assert len(points)==n and points[-1]==0
    assert all(a<b for a,b in zip(points,points[1:]))
    assert all(p<0 for p in points[:-1])
    signs=[sign_at(g,p,D) for p in points]
    assert signs==c['signs']
    assert all(a*b<0 for a,b in zip(signs,signs[1:]))
    # n-1 disjoint open negative intervals each contain a root. Degree n-1.
    print(f'n={n}: {n-1} distinct negative gamma roots certified')

A=F(65,192);B=F(195,64);L=F(0)
for j in range(1,9):
    q=F(5,4)*F(40,40-j)*A**j/factorial(j)
    for a in range(2*j):q*=F(80,80-a)**2
    L+=q
T=F(5,4)*B**9/factorial(9)/(1-B/10)
E=F(259,331)**20*(1+F(331,108*19))
large=F(5,4)*21*B**21/factorial(21)/(1-B/22)
constant=40*F(585,2560)**40
assert L+T<F(2,3)
assert E<F(1,50)
assert large<F(1,1000)
assert constant<F(1,1000)
assert F(2720,2187)>F(6,5)
assert F(233,243)*F(60,53)**2>F(6,5)
assert sum(F(6,5)**j/factorial(j) for j in range(5))>F(13,4)
assert F(1,50)+F(51,50)*F(2,3)+F(2,1000)==F(351,500)<1
print('All finite root certificates and analytic rational bounds pass')
