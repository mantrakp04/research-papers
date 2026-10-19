# Real Rootedness of Crown Order Polytope Numerators

Mantra Patel

10 October 2026

## Abstract

Let $C_{2n}$ be the height-two crown poset and let $H_n$ be the $h^*$-polynomial of its order polytope. Every zero of $H_n$ is shown to be negative and real for all $n\ge2$, with simple zeros when $n\ge3$ and $H_2(t)=(1+t)^2$. The statement addresses Conjecture 5.18 of Lundström and Saud Maia Leite in arXiv:2504.05123v5. A transfer-matrix spectrum produces alternating signs near the origin. An exact differential representation using the hyperbolic secant produces the remaining signs, with a uniform normalized error below $351/500$ for every $n\ge40$. Explicit overlap inequalities join the two sets of samples. The cases $3\le n\le39$ are proved by rational sign certificates and a standard-library integer and rational verifier included with the manuscript.

**Keywords:** crown poset; order polytope; real-rootedness; Ehrhart series; rational certificates.

<a id="the-family-and-the-statement"></a>

## 1 The family and the statement

For a finite poset $P$, use the increasing-coordinate convention 

$$
\mathcal O(P)=\{x\in[0,1]^P:x_u\le x_v\text{ whenever }u\le_Pv\}.
$$

 Its vertices are characteristic vectors of upper sets, and it is a full-dimensional lattice polytope in $\mathbb R^P$ \[[2](#ref-Stanley)\]. For $n\ge2$, define the crown $C_{2n}$ on $a_1,\ldots,a_n,b_1,\ldots,b_n$ by the cover relations 

$$
a_i<b_i,\qquad a_{i+1}<b_i\qquad (i\bmod n).
$$

 Thus $\mathcal O(C_{2n})$ has dimension $2n$. Define its lattice-point count and Ehrhart numerator by <a id="eq:definition"></a>

$$
L_n(m)=|m\mathcal O(C_{2n})\cap\mathbb Z^{2n}|,
 \qquad F_n(t)=\sum_{m\ge0}L_n(m)t^m=\frac{H_n(t)}{(1-t)^{2n+1}}.
$$

**Equation (1.1)**

Here $H_n(t)=h^*(\mathcal O(C_{2n}),t)$ and $H_n(0)=1$.

Lundström and Saud Maia Leite give a cyclic-swap interpretation of $H_n$ and establish its $\gamma$-nonnegativity \[[1](#ref-LSML), Theorems 5.11 and 5.19\]. They ask whether $H_n$ is real-rooted for every $n\ge2$ \[[1](#ref-LSML), Conjecture 5.18, p. 30\]. This citation refers to the latest inspected preprint, version 5 of 1 October 2026, which reports verification for $2\le n\le6$.

<a id="thm:main"></a>

**Theorem 1.1**. For every integer $n\ge2$, all zeros of $H_n$ are negative real numbers. Moreover, $H_2(t)=(1+t)^2$, and for every $n\ge3$, the polynomial $H_n$ has degree $2n-2$ and has $2n-2$ distinct zeros. Exactly $n-1$ lie in $(-1,0)$, and the other $n-1$ are their reciprocals in $(-\infty,-1)$.

The proof is analytic for $n\ge40$ and uses exact finite computation for $2\le n\le39$. The latter is a part of the proof, not numerical corroboration. Section [7](#sec:finite) specifies the certificate and exact checks; Appendix [A](#app:verifier) reproduces the verifier. No floating-point root decisions are used.

For $n\ge3$, the crown is the poset of nonempty proper faces of an $n$-gon. Adjoining a bottom and top gives the full polygon face lattice. The resulting twofold lattice-pyramid construction and preservation of the $h^*$-polynomial are established background \[[1](#ref-LSML), Proposition 6.1 and Theorem 6.6\]. The ordinary Ehrhart polynomials, however, differ. The distinction between the numerator and the ordinary Ehrhart polynomial is important: the present result concerns all-$n$ real-rootedness of the crown numerator.

The transfer trace formula is an established specialization of Huang’s circular-fence formula \[[4](#ref-Huang), Proposition 4.1\]. Dominant-term sign localization, secant partial fractions, Newton identities, and continuants are also classical; compare the central-index viewpoint in \[[5](#ref-FNS)\]. The proposed contribution is the uniform quantitative real-rootedness argument and its exact finite completion, not a new counting framework. Related zigzag Eulerian polynomials are studied in \[[3](#ref-PZ)\]; no conjecture about their real-rootedness is assumed here. Targeted searches on 7 October 2026 located no earlier all-$n$ proof of this crown result. Such searches do not establish novelty or rule out unpublished work.

<a id="sec:transfer"></a>

## 2 Transfer traces and reciprocal symmetry

For $N\ge1$, let $K_N=(\min(i,j))_{1\le i,j\le N}$ and $T_n(N)=\operatorname{tr}(K_N^n)$. The latter notation will also denote its polynomial extension in $N$, constructed below; set $T_n(0)=0$. The following counting identity is the alternating specialization of Huang’s circular-fence transfer formula \[[4](#ref-Huang), Proposition 4.1\]. With $M_+[a,b]=\mathbf1_{a\ge b}$ and $M_-=M_+^{\mathsf T}$ on $[N]$, one has $M_+M_-=K_N$. Huang’s cyclic product therefore becomes $\operatorname{tr}(K_N^n)$. Replacing the alphabet size $N$ by $m+1$ gives exactly the identity below. Its direct proof is retained for completeness.

<a id="lem:transfer"></a>

**Lemma 2.1**. For every $m\ge0$, $L_n(m)=T_n(m+1)$.

*Proof.* After assigning $x_i\in\{0,\ldots,m\}$ to $a_i$, there are $m+1-\max(x_i,x_{i+1})$ choices at $b_i$, independently for different $i$. With $y_i=m+1-x_i$, their total is 

$$
\sum_{y_1,\ldots,y_n=1}^{m+1}
 \min(y_1,y_2)\cdots\min(y_n,y_1)=\operatorname{tr}(K_{m+1}^n).
$$

 ◻

<a id="lem:determinant"></a>

**Lemma 2.2**. Let $w=2\arcsin(\sqrt z/2)$, expanded at $z=0$. Then <a id="eq:determinant"></a>

$$
\det(I-zK_N)=\sum_{j=0}^N(-z)^j\binom{N+j}{2j}
 =\frac{\cos((N+1/2)w)}{\cos(w/2)}.
$$

**Equation (2.1)**

For each $n\ge1$, $T_n(N)$ extends to a polynomial of degree $2n$, invariant under $N\mapsto-N-1$.

*Proof.* Write $K_N=U_NU_N^{\mathsf T}$, where $U_N$ is lower triangular with entries one on and below its diagonal. Thus $\det K_N=1$. Its inverse is tridiagonal with diagonal $2,\ldots,2,1$ and neighboring entries $-1$. Expansion from the end with entry $2-z$ gives 

$$
D_N=(2-z)D_{N-1}-D_{N-2},\quad D_0=1,\quad D_1=1-z,
$$

 where $D_N=\det(I-zK_N)$. Both expressions in [(2.1)](#eq:determinant) satisfy this recurrence and the initial conditions. For the cosine expression use $2-z=2\cos w$; for the sum use Pascal’s identity twice. Near zero, <a id="eq:trace-log"></a>

$$
-\log D_N(z)=\sum_{n\ge1}\frac{T_n(N)}n z^n.
$$

**Equation (2.2)**

Newton identities give a polynomial in $N$ at each coefficient. The cosine expression makes it even in $N+1/2$. The degree and positive leading coefficient follow explicitly from the next lemma. ◻

<a id="lem:shifted"></a>

**Lemma 2.3**. Put $Q_n(x)=T_n(x-1/2)$ and let $e_j$ be the elementary symmetric polynomial, with $e_0=1$. Then <a id="eq:Q"></a><a id="eq:c"></a><a id="eq:beta"></a>

$$
\begin{aligned}
 Q_n(x)&=-\frac1{2\cdot4^n}+\sum_{k=1}^n c_{n,k}x^{2k},\\
 c_{n,k}&=n\beta_k\frac{(2k)!}{(2n)!}
 e_{n-k}(1^2,2^2,\ldots,(n-1)^2),\\
 \beta_k&=\frac{(4^k-1)\zeta(2k)}{k\pi^{2k}}
 =\frac{(4/\pi^2)^k}{k}a_k,
 \qquad a_k=\sum_{r\ge0}(2r+1)^{-2k}.
\end{aligned}
$$

**Equations (2.3), (2.4), (2.5)**

In particular, <a id="eq:abounds"></a>

$$
1\le a_k\le\frac{\pi^2}{8}<\frac54,
 \qquad c_{n,n}=n\beta_n\ge(4/\pi^2)^n>0.
$$

**Equation (2.6)**

*Proof.* The classical cosine product, logarithmically expanded near zero, gives 

$$
\cos u=\prod_{r\ge0}\left(1-\frac{4u^2}{(2r+1)^2\pi^2}\right),
 \qquad -\log\cos u=\sum_{k\ge1}\beta_k u^{2k}.
$$

 Absolute convergence on sufficiently small closed disks justifies the expansion. The odd reciprocal sum gives [(2.5)](#eq:beta); it decreases with $k\ge1$ and equals $\pi^2/8$ at $k=1$.

The needed coefficient identity is <a id="eq:arcsin"></a>

$$
[z^n]w^{2k}=\frac{(2k)!}{(2n)!}
 e_{n-k}(1^2,\ldots,(n-1)^2),\qquad 1\le k\le n.
$$

**Equation (2.7)**

Indeed $\psi(z)=\cos(xw(z))$ satisfies 

$$
z(4-z)\psi''+(2-z)\psi'+x^2\psi=0.
$$

 For $d_j=[z^j]\psi$, with $d_0=1$, this gives 

$$
d_{j+1}=\frac{j^2-x^2}{2(j+1)(2j+1)}d_j,
 \qquad d_n=\frac{(-1)^nx^2\prod_{j=1}^{n-1}(x^2-j^2)}{(2n)!}.
$$

 Compare coefficients of $x^{2k}$ with the cosine series to obtain [(2.7)](#eq:arcsin). Now 

$$
Q_n(x)=n[z^n]\{-\log\cos(xw)+\log\cos(w/2)\}.
$$

 Since $\log\cos(w/2)=\tfrac12\log(1-z/4)$, its contribution is $-1/(2\cdot4^n)$. The other term gives [(2.4)](#eq:c). ◻

The degree and symmetry in the next proposition are already established in \[[1](#ref-LSML), Corollaries 5.13 and 5.16\]. The generating-function proof below keeps the later root count self-contained.

<a id="prop:palindrome"></a>

**Proposition 2.4**. The polynomial $H_n$ is monic of degree $2n-2$ and satisfies <a id="eq:reciprocal"></a>

$$
H_n(t)=t^{2n-2}H_n(1/t).
$$

**Equation (2.8)**

*Proof.* Set $C(m)=T_n(m+1)$. Evenness gives $C(-m-3)=C(m)$ and $C(-1)=C(-2)=0$. For every polynomial $C$, its rational generating function has expansion at infinity 

$$
\sum_{m\ge0}C(m)t^m=-\sum_{m\ge1}C(-m)t^{-m}.
$$

 For $C=1$ this is the geometric series identity; applying $t\,\mathrm d/\mathrm dt$ repeatedly proves it for monomials and hence every polynomial. Therefore 

$$
F_n(1/t)=-\sum_{m\ge1}C(-m)t^m=-t^3\sum_{m\ge0}C(m)t^m=-t^3F_n(t).
$$

 Since $C$ has degree $2n$, [(1.1)](#eq:definition) has a polynomial numerator of degree at most $2n$. Substitution of this rational identity gives [(2.8)](#eq:reciprocal). Together with $H_n(0)=1$, it proves the asserted degree and leading coefficient. ◻

<a id="sec:outer"></a>

## 3 Outer signs from spectral dominance

<a id="lem:spectrum"></a>

**Lemma 3.1**. The eigenvalues of $K_N$ are <a id="eq:spectrum"></a>

$$
\lambda_{N,j}=\frac1{4\sin^2((2j-1)\pi/(4N+2))},\qquad 1\le j\le N.
$$

**Equation (3.1)**

Writing $\lambda_N=\lambda_{N,1}$, uniformly for $N\ge1$ and $n\ge2$, <a id="eq:trace-bound"></a>

$$
1\le T_n(N)/\lambda_N^n<9/8.
$$

**Equation (3.2)**

*Proof.* The inverse matrix has sine eigenvectors $v_i=\sin(i\alpha)$ with eigenvalue $2-2\cos\alpha$. Its boundary conditions are $v_0=0$ and $v_{N+1}=v_N$, giving $\alpha=(2j-1)\pi/(2N+1)$ and [(3.1)](#eq:spectrum). The bounds $\sin u\le u$ and $\sin u\ge2u/\pi$ on $[0,\pi/2]$ imply 

$$
\lambda_{N,j}/\lambda_N\le(\pi/(2(2j-1)))^2.
$$

 For $j\ge2$ this is below one, so 

$$
\frac{T_n(N)}{\lambda_N^n}
 \le1+\frac{\pi^4}{16}\sum_{j\ge2}(2j-1)^{-4}
 \le1+\frac{\pi^4}{864}<\frac98.
$$

 The sum is at most $1/81+\int_2^\infty(2x-1)^{-4}\,\mathrm dx=1/54$, and $\pi^2<10$ proves strictness. ◻

Extend $\lambda_x=[4\sin^2(\pi/(4x+2))]^{-1}$ to real $x\ge1$ and put $f(x)=\log\lambda_x$. Define <a id="eq:outer-def"></a>

$$
D_k=f(k+1)-\frac{f(k)+f(k+2)}2,\quad
 r_k=\exp\frac{f(k)-f(k+2)}2,\quad s_k^{\rm out}=-n\log r_k.
$$

**Equation (3.3)**

<a id="lem:curvature"></a>

**Lemma 3.2**. The function $f$ is increasing and strictly concave, and <a id="eq:Dstrong"></a><a id="eq:Dweak"></a>

$$
\begin{aligned}
 D_k&\ge\left(1-\frac{\pi^2}{12(k+1/2)^2}\right)
 \left[-\log\left(1-\frac1{(k+3/2)^2}\right)\right]\\
 &>\frac{1-\pi^2/(12(k+1/2)^2)}{(k+3/2)^2}.
\end{aligned}
$$

**Equations (3.4), (3.5)**

*Proof.* Put $y=x+1/2$ and $u=\pi/(4y)\le\pi/6$. Then 

$$
f'(x)=\frac{2u\cot u}{y}>0,\quad
 -f''(x)=\frac2{y^2}(2u\cot u-u^2\csc^2u).
$$

 The parenthetical expression is $u(\sin(2u)-u)/\sin^2u$. Its numerator obeys $\sin(2u)-u\ge u-(4/3)u^3>0$. Using $\sin^2u\le u^2$ gives <a id="eq:curvature"></a>

$$
-f''(x)\ge\frac2{(x+1/2)^2}
 \left(1-\frac{\pi^2}{12(x+1/2)^2}\right)>0.
$$

**Equation (3.6)**

The centered second difference is 

$$
D_k=\frac12\int_{-1}^{1}(1-|v|)(-f''(k+1+v))\,\mathrm dv.
$$

 Bound the factor in parentheses in [(3.6)](#eq:curvature) by its minimum on the interval, and use 

$$
\int_{-1}^{1}\frac{1-|v|}{(k+3/2+v)^2}\,\mathrm dv
 =-\log\left(1-\frac1{(k+3/2)^2}\right).
$$

 This proves [(3.4)](#eq:Dstrong); $-\log(1-z)>z$ proves [(3.5)](#eq:Dweak). ◻

<a id="lem:outer-sign"></a>

**Lemma 3.3**. The numbers $r_k$ satisfy $0<r_1<r_2<\cdots<1$. If $nD_k\ge\log(13/4)$, then <a id="eq:outer-sign"></a>

$$
\operatorname{sgn}H_n(-r_k^n)=(-1)^k.
$$

**Equation (3.7)**

*Proof.* Strict concavity gives the ordering. For fixed $k$, put $a_m=\lambda_{m+1}^nr_k^{nm}$. Its consecutive ratios decrease with $m$, and $a_{k-1}/a_k=a_{k+1}/a_k=q=e^{-nD_k}$. Thus 

$$
\sum_{m\ne k}a_m\le\frac{2q}{1-q}a_k.
$$

 In $F_n(-r_k^n)=\sum_{m\ge0}(-1)^mT_n(m+1)r_k^{nm}$, [(3.2)](#eq:trace-bound) bounds the absolute sum of terms other than the $k$th strictly below $(9/8)2q a_k/(1-q)$. This is at most $a_k$ when $q\le4/13$, whereas the $k$th term has magnitude at least $a_k$. Its sign therefore prevails. Multiplication by $(1+r_k^n)^{2n+1}>0$ proves the claim. ◻

<a id="prop:outer-range"></a>

**Proposition 3.4**. For $n\ge40$, put <a id="eq:K"></a>

$$
K=\left\lfloor\frac45\sqrt n\right\rfloor-1.
$$

**Equation (3.8)**

Then $K\ge4$, and [(3.7)](#eq:outer-sign) holds for $1\le k\le K$.

*Proof.* For $1\le k\le3$, [(3.5)](#eq:Dweak) and $\pi^2<10$ give 

$$
nD_k>40\cdot\frac{17}{27}\cdot\frac4{81}=\frac{2720}{2187}>\frac65.
$$

 For $4\le k\le K$, its first factor is greater than $233/243$. Since $k+3/2\le(4/5)\sqrt n+1/2$ and $\sqrt n>6$, 

$$
nD_k>\frac{233}{243}\left(\frac{60}{53}\right)^2>\frac65.
$$

 Finally $\sum_{j=0}^4(6/5)^j/j!>13/4$, so $\log(13/4)<6/5$. Apply Lemma [3.3](#lem:outer-sign). ◻

<a id="sec:poles"></a>

## 4 The secant representation and pole expansion

Set $g(s)=1/(2\cosh(s/2))$ and $\partial_s=\mathrm d/\mathrm ds$.

<a id="lem:operator"></a>

**Lemma 4.1**. For $s\ge0$, <a id="eq:operator"></a>

$$
Q_n(\partial_s)g(s)=-e^{-3s/2}F_n(-e^{-s}).
$$

**Equation (4.1)**

Consequently $H_n(-e^{-s})$ and $Q_n(\partial_s)g(s)$ have opposite signs whenever nonzero.

*Proof.* For $s>0$, $g(s)=\sum_{l\ge0}(-1)^le^{-(l+1/2)s}$, with locally uniformly convergent derivatives of every fixed order. Since $Q_n$ is even, 

$$
Q_n(\partial_s)g(s)=\sum_{l\ge0}(-1)^lT_n(l)e^{-(l+1/2)s}.
$$

 The $l=0$ term vanishes. Reindex $l=m+1$ to obtain [(4.1)](#eq:operator). Both sides extend continuously to $s=0$, since $F_n$ is rational with its only possible pole at $t=1$. Equation [(1.1)](#eq:definition) gives the sign statement. ◻

<a id="lem:poles"></a>

**Lemma 4.2**. For $k\ge1$ and $s\ge0$, an absolutely convergent expansion is <a id="eq:poles"></a>

$$
g^{(2k)}(s)=2(2k)!\sum_{r\ge0}(-1)^r
 \operatorname{Im}(s-i(2r+1)\pi)^{-2k-1}.
$$

**Equation (4.2)**

Put $R=(s^2+\pi^2)^{1/2}$ and $\theta=\arg(s+i\pi)\in(0,\pi/2]$. Its $r=0$ term equals $2(2k)!R^{-2k-1}\sin((2k+1)\theta)$.

*Proof.* First, <a id="eq:fourier"></a>

$$
g(s)=\int_0^\infty\frac{\cos(sx)}{\cosh(\pi x)}\,\mathrm dx.
$$

**Equation (4.3)**

Integrate $e^{isz}/\cosh(\pi z)$ on a rectangle with horizontal sides on $\mathbb R$ and $\mathbb R+i$. The vertical sides tend to zero. Shifting by $i$ multiplies the integrand by $-e^{-s}$, while the pole at $i/2$ has residue $e^{-s/2}/(\pi i)$. If $I$ is the full real-line integral, $(1+e^{-s})I=2e^{-s/2}$. Its real even half is [(4.3)](#eq:fourier).

Differentiate $2k$ times and expand $1/\cosh(\pi x)=2\sum_{r\ge0}(-1)^re^{-(2r+1)\pi x}$. For $k\ge1$, termwise integration is justified by 

$$
\sum_{r\ge0}\int_0^\infty x^{2k}e^{-(2r+1)\pi x}\,\mathrm dx
 =(2k)!\sum_{r\ge0}((2r+1)\pi)^{-2k-1}<\infty.
$$

 The resulting Laplace integral is $2(-1)^k(2k)!\sum_r(-1)^r\operatorname{Re}((2r+1)\pi-is)^{-2k-1}$, equal to [(4.2)](#eq:poles). Polar coordinates give the last assertion. ◻

<a id="sec:error"></a>

## 5 Uniform control of the central error

Throughout this section assume <a id="eq:central-region"></a>

$$
n\ge40,\qquad 0\le s\le\frac52\sqrt n,\qquad R^2=s^2+\pi^2<\frac{13}2n.
$$

**Equation (5.1)**

All bounds are uniform on this region. Define 

$$
E_k(s)=\sum_{r\ge1}
 \left(\frac{s^2+\pi^2}{s^2+(2r+1)^2\pi^2}\right)^{k+1/2}.
$$

<a id="lem:tails"></a>

**Lemma 5.1**. If $k\ge n/2$, then $E_k(s)<1/50$. For all $k\ge1$, <a id="eq:coarse"></a>

$$
1+E_k(s)\le1+\frac R{2\pi}<1+\sqrt n.
$$

**Equation (5.2)**

*Proof.* The ratios are below one and increase with $s^2$. For $k\ge n/2$, 

$$
E_k(s)\le\sum_{r\ge1}
 \left(\frac{(25/4)n+\pi^2}{(25/4)n+(2r+1)^2\pi^2}\right)^{n/2}.
$$

 For $b>a>0$, $n\log((n+a)/(n+b))$ strictly decreases: with $v=(b-a)/(n+a)>0$, its derivative is $-\log(1+v)+[n/(n+a)]v/(1+v)<0$. Each summand therefore decreases with $n$; it also decreases with $\pi^2$. Substituting $n=40$ and $\pi^2>9$ gives <a id="eq:pole-rational"></a>

$$
E_k(s)\le\sum_{r\ge1}\left(\frac{259}{250+9(2r+1)^2}\right)^{20}
 \le\left(\frac{259}{331}\right)^{20}
 \left(1+\frac{331}{108\cdot19}\right)<\frac1{50}.
$$

**Equation (5.3)**

For the middle inequality, bound the decreasing summand by its first value plus its integral over $[1,\infty)$. The tangent bound $250+9(2x+1)^2\ge331+108(x-1)$ gives the stated integral.

For arbitrary $k\ge1$, use $s^2+(2r+1)^2\pi^2\ge R^2+4r^2\pi^2$ and sum by an integral: 

$$
1+E_k(s)\le\sum_{r\ge0}(1+4\pi^2r^2/R^2)^{-3/2}
 \le1+\int_0^\infty(1+4\pi^2x^2/R^2)^{-3/2}\,\mathrm dx
 =1+\frac R{2\pi}.
$$

 The final inequality in [(5.2)](#eq:coarse) follows from [(5.1)](#eq:central-region) and $\pi^2>9$. ◻

Normalize by the positive leading nearest-pole scale <a id="eq:M"></a>

$$
M=2c_{n,n}(2n)!R^{-2n-1}.
$$

**Equation (5.4)**

For $j=n-k\in\{1,\ldots,n-1\}$, the normalized absolute contribution of $c_{n,k}g^{(2k)}$ is at most $b_{n,j}(1+E_k(s))$, where <a id="eq:b"></a>

$$
b_{n,j}=\frac{\beta_{n-j}}{\beta_n}
 \left(\frac{(2n-2j)!}{(2n)!}\right)^2
 e_j(1^2,\ldots,(n-1)^2)R^{2j}.
$$

**Equation (5.5)**

The two factorial ratios come respectively from [(2.4)](#eq:c) and the derivative scale in [(4.2)](#eq:poles).

<a id="lem:all-j"></a>

**Lemma 5.2**. With $(n)_j=n(n-1)\cdots(n-j+1)$ and $B=195/64$, for every $1\le j\le n-1$, <a id="eq:all-j"></a>

$$
b_{n,j}\le\frac54\frac{(\pi^2R^2/64)^j}{j!(n)_j}
 \le\frac54\frac{B^j}{j!}.
$$

**Equation (5.6)**

*Proof.* Each term in $e_j$ is at most the product of its $j$ largest arguments, giving $e_j\le\binom{n-1}{j}((n-1)_j)^2$. Pair the denominator factors in $(2n)!/(2n-2j)!$ as $(2r)(2r-1)$, where $n-j+1\le r\le n$. Since 

$$
\frac{r-1}{(2r)(2r-1)}\le\frac1{4r},\qquad
 e_j\left(\frac{(2n-2j)!}{(2n)!}\right)^2
 \le\frac{\binom{n-1}{j}}{16^j(n)_j^2},
$$

 combine 

$$
\frac{\beta_{n-j}}{\beta_n}\le\frac54\frac n{n-j}\left(\frac{\pi^2}4\right)^j,
 \qquad \binom{n-1}{j}=\frac{n-j}{n}\frac{(n)_j}{j!}.
$$

 The cancellation of $n/(n-j)$ proves the first bound.

The geometric mean of the largest $j$ integers in $\{1,\ldots,n\}$ is at least that of all $n$. Also $n!\ge(n/e)^n$, by integrating $\log x$. Thus $(n)_j\ge(n/e)^j$. Using $e<3$, $\pi^2<10$, and $R^2/n<13/2$ gives $B=3\cdot10\cdot(13/2)/64=195/64$. ◻

<a id="lem:small-j"></a>

**Lemma 5.3**. Uniformly on [(5.1)](#eq:central-region), <a id="eq:small-j-total"></a>

$$
\sum_{j=1}^{\lfloor n/2\rfloor}b_{n,j}<\frac23.
$$

**Equation (5.7)**

*Proof.* For the first eight terms use 

$$
e_j\le\frac{(\sum_{r=1}^{n-1}r^2)^j}{j!}<\frac{(n^3/3)^j}{j!}.
$$

 In the expanded power, each product with distinct indices occurs $j!$ times. With $A=65/192$, substitution into [(5.5)](#eq:b) yields, for $1\le j\le8$, 

$$
\begin{aligned}
 b_{n,j}&\le\frac54\frac n{n-j}\frac{A^j}{j!}
 \prod_{a=0}^{2j-1}\left(\frac{2n}{2n-a}\right)^2\\
 &\le\frac54\frac{40}{40-j}\frac{A^j}{j!}
 \prod_{a=0}^{2j-1}\left(\frac{80}{80-a}\right)^2.
\end{aligned}
$$

 The power before the product is bounded using $\pi^2R^2/(192n)<65/192$; the remaining factors decrease with $n$. Call the sum of these eight rational bounds $L$. For $j\ge9$, successive terms of the factorial majorant in [(5.6)](#eq:all-j) have ratio at most $B/10<1$. Hence <a id="eq:LT"></a>

$$
\sum_{j=1}^{\lfloor n/2\rfloor}b_{n,j}\le L+T<\frac23,
 \qquad T=\frac54\frac{B^9}{9!(1-B/10)}.
$$

**Equation (5.8)**

This finite rational inequality is reproduced in Appendix [A](#app:verifier). For scale only, $L\approx0.547471$ and $T\approx0.112114$, giving $L+T\approx0.659585$; these decimals are not proof premises. ◻

<a id="lem:large-j"></a>

**Lemma 5.4**. The total normalized contribution with $j>n/2$ is less than $1/1000$. The normalized constant-term contribution is also less than $1/1000$.

*Proof.* Put $m=\lfloor n/2\rfloor+1\ge21$. Then $n<2m$ and $1+\sqrt n\le m$. Equations [(5.2)](#eq:coarse) and [(5.6)](#eq:all-j) bound the large-$j$ contribution by <a id="eq:large-j"></a>

$$
\frac54\frac{mB^m}{m!(1-B/(m+1))}
 \le\frac54\frac{21B^{21}}{21!(1-B/22)}<\frac1{1000}.
$$

**Equation (5.9)**

This decreases for integer $m\ge21$, since $mB^m/m!=B^m/(m-1)!$ has consecutive ratio $B/m<1$, while $1-B/(m+1)$ increases.

Using $g(s)\le1/2$ and [(2.6)](#eq:abounds), the constant term in [(2.3)](#eq:Q), divided by $M$, is bounded by <a id="eq:constant"></a>

$$
\frac R{8(2n)!}\left(\frac{\pi^2R^2}{16}\right)^n
 \le n\left(\frac{585}{64n}\right)^n
 \le40\left(\frac{585}{2560}\right)^{40}<\frac1{1000}.
$$

**Equation (5.10)**

The first inequality uses $(2n)!\ge(2n/e)^{2n}$, $e<3$, $R^2/n<13/2$, $\pi^2<10$, and $R/8\le n$. The middle expression has logarithmic derivative $1/n+\log(585/(64n))-1<0$ for $n\ge40$. Both final rational comparisons are checked in Appendix [A](#app:verifier). ◻

<a id="prop:central-error"></a>

**Proposition 5.5**. Throughout [(5.1)](#eq:central-region), <a id="eq:central-error"></a>

$$
\left|\frac{Q_n(\partial_s)g(s)}M-\sin((2n+1)\theta)\right|
 <\frac{351}{500}<1.
$$

**Equation (5.11)**

*Proof.* The leading derivative has pole tail below $1/50$. For $1\le j\le\lfloor n/2\rfloor$, $k=n-j\ge n/2$, so Lemmas [5.1](#lem:tails) and [5.3](#lem:small-j) bound their combined contribution by $(51/50)(2/3)$. The remaining derivatives and constant term contribute less than $1/1000$ each. The sum is 

$$
\frac1{50}+\frac{51}{50}\frac23+\frac1{1000}+\frac1{1000}=\frac{351}{500}.
$$

 ◻

<a id="sec:join"></a>

## 6 Joining the signs and exhausting the degree

For $0\le\ell\le n$, set <a id="eq:central-samples"></a>

$$
\theta_\ell=\frac{(\ell+1/2)\pi}{2n+1},\qquad s_\ell=\pi\cot\theta_\ell.
$$

**Equation (6.1)**

They obey $s_0>s_1>\cdots>s_n=0$. If $s_\ell\le(5/2)\sqrt n$, Proposition [5.5](#prop:central-error) and $\sin((2n+1)\theta_\ell)=(-1)^\ell$ give, by Lemma [4.1](#lem:operator), <a id="eq:central-sign"></a>

$$
\operatorname{sgn}H_n(-e^{-s_\ell})=(-1)^{\ell+1}.
$$

**Equation (6.2)**

<a id="lem:join"></a>

**Lemma 6.1**. For $n\ge40$ and $K$ in [(3.8)](#eq:K), $K+2\le n$. All $s_\ell$ with $K+2\le\ell\le n$ are central, and $s_K^{\rm out}>s_{K+2}$.

*Proof.* The first claim follows from $K+2\le(4/5)\sqrt n+1\le n$. Also $K+5/2\ge(4/5)\sqrt n+1/2$. Since $\cot x<1/x$ on $(0,\pi/2]$, 

$$
0\le s_\ell\le s_{K+2}<\frac{2n+1}{K+5/2}\le\frac52\sqrt n.
$$

 For the last inequality, multiplying the lower denominator bound by $(5/2)\sqrt n$ gives $2n+(5/4)\sqrt n\ge2n+1$.

Use $u\cot u\ge\cos u\ge1-u^2/2$ and integrate $f'$ over $[K,K+2]$. Put $a=K+3/2$ and $\delta=\pi^2/(32(K+1/2)^2)$. Then 

$$
s_K^{\rm out}=\frac n2\int_K^{K+2}f'(x)\,\mathrm dx
 \ge n(1-\delta)\log\frac{a+1}{a-1}
 \ge\frac{2n}{a}(1-\delta).
$$

 Here $\log((a+1)/(a-1))\ge2/a$, by the series for $\operatorname{arctanh}(1/a)$. The last expression exceeds $(2n+1)/(a+1)$: the difference has positive denominator and numerator 

$$
2n-a-2n\delta(a+1)>n-a>0.
$$

 Indeed $a<n$ throughout the range, and $\delta(a+1)<1/2$ follows from $16(K+1/2)^2>\pi^2(K+5/2)$. Replacing $\pi^2$ by $10$, the difference becomes $16K^2+6K-21$, positive and increasing for integers $K\ge1$. Thus 

$$
s_K^{\rm out}>\frac{2n+1}{K+5/2}>s_{K+2}.
$$

 ◻

*Proof of Theorem [1.1](#thm:main) for $n\ge40$.* Move from $t=0$ toward $t=-1$. Proposition [3.4](#prop:outer-range) gives successive outer points $-r_k^n$, $1\le k\le K$, with signs $(-1)^k$. Together with $H_n(0)=1$, these give $K$ disjoint open intervals containing roots in $(-1,0)$.

By Lemma [6.1](#lem:join), the first central point $-e^{-s_{K+2}}$ comes after the last outer point in this traversal; its sign $(-1)^{K+3}$ is opposite to $(-1)^K$. The central points $\ell=K+2,\ldots,n$ then alternate in sign, ending at $t=-1$. There are $n-K-1$ such points. The transition interval and intervals between successive central points therefore give $n-K-1$ additional roots. The endpoint $-1$ has nonzero sign. Altogether this gives $n-1$ distinct roots in $(-1,0)$.

By Proposition [2.4](#prop:palindrome), their distinct reciprocals lie in $(-\infty,-1)$. These two disjoint sets exhaust degree $2n-2$. All roots are consequently negative and simple. ◻

<a id="sec:finite"></a>

## 7 Exact certification of the remaining cases

A palindromic polynomial of degree $2n-2$ has a unique expansion <a id="eq:gamma"></a>

$$
H_n(t)=\sum_{j=0}^{n-1}\gamma_{n,j}t^j(1+t)^{2n-2-2j}
 =(1+t)^{2n-2}\Gamma_n\left(\frac{t}{(1+t)^2}\right),
$$

**Equation (7.1)**

where $\Gamma_n(x)=\sum_j\gamma_{n,j}x^j$. Successively eliminate the coefficient of $t^j$; symmetry eliminates the matching highest coefficient. This proves existence and uniqueness. The initial cases are 

$$
H_2(t)=(1+t)^2,\quad \Gamma_3(x)=1+7x+4x^2,\quad
 \Gamma_4(x)=1+32x+120x^2+32x^3.
$$

<a id="lem:gamma-roots"></a>

**Lemma 7.1**. If $\Gamma_n$ has $n-1$ distinct negative roots and degree $n-1$, then $H_n$ has $2n-2$ distinct negative roots, one reciprocal pair for each root of $\Gamma_n$.

*Proof.* For a negative root $y$, the equation $t/(1+t)^2=y$ is $yt^2+(2y-1)t+y=0$. Its discriminant is $1-4y>0$, its root product is $1$, and its root sum is $(1-2y)/y<0$. Thus it has two distinct negative roots, neither equal to $-1$, one in $(-1,0)$ and one below $-1$. Different $y$ give disjoint pairs because $t/(1+t)^2$ is single-valued away from $-1$. These roots belong to $H_n$ by [(7.1)](#eq:gamma) and exhaust its degree. ◻

<a id="regenerating-the-coefficients"></a>

### 7.1 Regenerating the coefficients

For a fixed positive integer $N$, let $e_j(N)=\binom{N+j}{2j}$, zero for $j>N$. Newton identities applied to [(2.1)](#eq:determinant) give the integer recurrence <a id="eq:newton"></a>

$$
p_r(N)=\sum_{j=1}^{r-1}(-1)^{j-1}e_j(N)p_{r-j}(N)
 +(-1)^{r-1}r e_r(N),\qquad r\ge1,
$$

**Equation (7.2)**

where $p_r(N)=T_r(N)$ and empty sums are zero. Then <a id="eq:hcoeff"></a>

$$
h_{n,k}=\sum_{j=0}^k(-1)^j\binom{2n+1}{j}T_n(k-j+1),\qquad 0\le k\le2n.
$$

**Equation (7.3)**

The verifier checks that the last two vanish, and obtains the $\gamma$-coefficients by exact triangular subtraction in [(7.1)](#eq:gamma). It does not trust stored $h^*$- or $\gamma$-coefficients.

<a id="certificate-and-verification-proposition"></a>

### 7.2 Certificate and verification proposition

The supplementary `finite_sign_certificates.json` has one record per $n=3,\ldots,39$. Each gives a positive denominator $D$, exactly $n$ integer numerators 

$$
p_0<p_1<\cdots<p_{n-1}=0,\qquad p_j<0\quad(j<n-1),
$$

 and signs of $\Gamma_n(p_j/D)$. Stored coefficients are redundant and are compared with regenerated ones. The file uses $D=2^{128}$; its SHA-256 digest is the concatenation of these two lines:

9bb119f040fa1a8e883c9e6a648257f934  
46f3e6e5e1af5c940c1371d481e4d6

<a id="prop:finite"></a>

**Proposition 7.2** (Exact finite computation). For $3\le n\le39$, the supplied certificate passes the verifier in Appendix [A](#app:verifier). Each $\Gamma_n$ has degree $n-1$ and nonzero alternating signs at its $n$ certified points. It therefore has $n-1$ distinct negative roots.

*Proof.* The verifier regenerates [(7.2)](#eq:newton)–[(7.3)](#eq:hcoeff), checks the degree and symmetry of $H_n$, and constructs [(7.1)](#eq:gamma). For $\Gamma_n(x)=a_0+\cdots+a_dx^d$, its function `sign_at` uses integer Horner arithmetic to evaluate the sign of 

$$
D^d\Gamma_n(p/D)=a_dp^d+a_{d-1}p^{d-1}D+\cdots+a_0D^d.
$$

 Since $D>0$, this is the exact sign required. It checks all endpoint order and sign conditions above. All checks pass for the supplied file, establishing 740 disjoint negative root intervals in total across the 37 polynomials. The intermediate value theorem produces $n-1$ distinct negative roots of each degree-$n-1$ polynomial and leaves no other roots. ◻

For example, the $n=3$ points are $-2,-1/2,0$, with signs $+,-,+$. The other records apply the same exact sign test. No extrapolation or unproved interlacing property is used; the auxiliary numerical process used to find possible endpoints is irrelevant to verification.

*Completion of the proof of Theorem [1.1](#thm:main).* Direct computation gives $H_2=(1+t)^2$. For $3\le n\le39$, combine Proposition [7.2](#prop:finite) with Lemma [7.1](#lem:gamma-roots). Section [6](#sec:join) proves the assertion for every $n\ge40$. ◻

<a id="reproducibility-and-scope"></a>

## 8 Reproducibility and scope

The package contains this manuscript, the certificate, and `verify_full_certificate.py`. Run the latter with Python 3 from any working directory; it finds the adjacent JSON file relative to its own location. It uses only the standard library and no network access. Do not use `-O`, which disables assertions. Its successful final output is

All finite root certificates and analytic rational bounds pass

The script verifies the finite roots and every finite rational comparison in the analytic estimates. It does not mechanically check the symbolic analytic arguments; these are supplied in Sections [2](#sec:transfer)–[6](#sec:join).

A separately implemented calculation reconstructed the finite polynomials using shifted-cosine coefficients and rational Sturm sequences through $n=40$. The finite computations check the certificates and the explicit rational bounds. The all-size conclusion also uses the symbolic identities, analytic inequalities, and sample-ordering argument supplied above; it is not inferred from a finite-range numerical test.

<a id="app:verifier"></a>

## A Exact verifier

The following is the complete supplementary verifier. Its assertions specify the finite certificate checks and the rational inequalities used above.

``` python
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
```

## References

<a id="ref-LSML"></a>

**\[1\]**

T. Lundström and L. Saud Maia Leite, *Order polytopes of crown posets*, European Journal of Combinatorics **133** (2026), 104304. [doi:10.1016/j.ejc.2025.104304](https://doi.org/10.1016/j.ejc.2025.104304). Latest inspected preprint: [arXiv:2504.05123v5](https://arxiv.org/abs/2504.05123v5), 1 October 2026.

<a id="ref-Stanley"></a>

**\[2\]**

R. P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry **1** (1986), 9–23. [Author-hosted paper](https://math.mit.edu/~rstan/pubs/pubfiles/66.pdf).

<a id="ref-PZ"></a>

**\[3\]**

T. K. Petersen and Y. Zhuang, *Zig-zag Eulerian polynomials*, European Journal of Combinatorics **124** (2025), 104073. [arXiv:2403.07181v4](https://arxiv.org/abs/2403.07181v4).

<a id="ref-Huang"></a>

**\[4\]**

P. C. Huang, *Bernstein Transfers and Greedy Records for Fence and Circular-Fence Order Polynomials*, [arXiv:2607.22767v2](https://arxiv.org/abs/2607.22767v2), 31 July 2026.

<a id="ref-FNS"></a>

**\[5\]**

J. Forsgård, D. Novikov and B. Shapiro, *A tropical analog of Descartes’ rule of signs*, [arXiv:1510.03257](https://arxiv.org/abs/1510.03257), 2015.
