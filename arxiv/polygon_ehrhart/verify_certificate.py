"""Exact certificate for the 13-gon Ehrhart counterexample. Python 3 stdlib only.
All arithmetic is integer or Fraction; no floating-point decisions are made.
"""
from fractions import Fraction as Q
from math import comb

HALF_H = [1, 271416, 1378078419, 837258390856, 131296310558015,
          7724454986455746, 209821561170879574, 2985931198521851042,
          24154691761269157097, 117280290847971630454,
          354406898580482272679, 682213052793220234662,
          847462155807564227086]

def trace_power(n, N):
    # Newton sums from det(I-z K_N) = sum_j (-z)^j C(N+j, 2j).
    e = [comb(N+j, 2*j) if j <= N else 0 for j in range(n+1)]
    p = [N]
    for k in range(1, n+1):
        p.append(sum((-1)**(j-1)*e[j]*p[k-j] for j in range(1,k))
                 + (-1)**(k-1)*k*e[k])
    return p[n]

def hstar(n):
    vals = [trace_power(n, m+1) for m in range(2*n+1)]
    h = [sum((-1)**j*comb(2*n+1,j)*vals[k-j] for j in range(k+1))
         for k in range(2*n+1)]
    assert h[-2:] == [0,0]
    return h[:-2]

def ehrhart_coefficients(n):
    # Values of the twofold lattice pyramid, followed by Newton interpolation.
    vals=[]; a=b=0
    for m in range(2*n+3):
        a += trace_power(n,m+1); b += a; vals.append(b)
    diffs=[]
    while vals:
        diffs.append(vals[0]); vals=[b-a for a,b in zip(vals,vals[1:])]
    out=[Q(0)]*len(diffs); basis=[Q(1)]
    for k, c in enumerate(diffs):
        for j, v in enumerate(basis): out[j] += c*v
        nxt=[Q(0)]*(len(basis)+1)
        for j,v in enumerate(basis):
            nxt[j] -= Q(k,k+1)*v; nxt[j+1] += v/Q(k+1)
        basis=nxt
    return out

def gamma_coefficients(h):
    d=len(h)-1; rem=h[:]; g=[]
    for j in range(d//2+1):
        c=rem[j];g.append(c)
        for k in range(j,d-j+1): rem[k]-=c*comb(d-2*j,k-j)
    assert not any(rem)
    return g

def eval_poly(coeffs,x):
    out=Q(0)
    for c in reversed(coeffs):out=out*x+c
    return out

if __name__ == '__main__':
    h=hstar(13)
    assert h == HALF_H + HALF_H[-2::-1]
    linear=sum((Q(1,j) for j in range(1,29)),Q(0))
    linear+=sum((Q((-1)**(j-1)*h[j],j*comb(28,j))
                 for j in range(1,len(h))),Q(0))
    assert linear == -Q(298495711,35302608)
    assert ehrhart_coefficients(13)[1] == linear
    assert [i for i,c in enumerate(ehrhart_coefficients(13)) if c<0]==[1]
    assert all(c>0 for i,c in enumerate(ehrhart_coefficients(13)) if i!=1)
    for n in range(3,13):
        assert all(c>0 for c in ehrhart_coefficients(n))
    g=gamma_coefficients(h)
    intervals=[(-30,-29),(-4,-3),(-2,-1),
       (-Q(1,2),-Q(1,3)),(-Q(1,4),-Q(1,5)),
       (-Q(1,8),-Q(1,9)),(-Q(1,17),-Q(1,18)),
       (-Q(1,39),-Q(1,40)),(-Q(1,111),-Q(1,112)),
       (-Q(1,472),-Q(1,473)),(-Q(1,4485),-Q(1,4486)),
       (-Q(1,4486),0)]
    assert len(g)==13 and g[-1]>0
    for a,b in intervals:
        assert a<b<=0
        assert eval_poly(g,Q(a))*eval_poly(g,Q(b))<0
    print('Verified: dimension 28; linear Ehrhart coefficient =',linear)
    print('Verified: all other Ehrhart coefficients are positive')
    print('Verified: all coefficients positive for polygons with 3 through 12 vertices')
    print('Verified: h* has 24 distinct negative real roots')
