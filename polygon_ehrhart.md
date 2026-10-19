# A Negative Ehrhart Coefficient for the Order Polytope of a Polygon Face Lattice

Mantra Patel

10 October 2026

## Abstract

Let $P_n$ be a convex $n$-gon and let $Q_n$ be the order polytope of its full face lattice, including the empty face and $P_n$ itself. Using established transfer-matrix counting formulas, exact coefficient extraction gives $[t]E_{13}(t)=-298495711/35302608$, where $E_n$ is the Ehrhart polynomial of $Q_n$. Thus the 28-dimensional polytope $Q_{13}$ is not Ehrhart-nonnegative. This gives a negative answer to the question stated as Question 6.5 in arXiv:2504.05123v5. The proof includes a counting formula derived from the poset inequalities, an integer recurrence for matrix traces, and a compact exact coefficient certificate. An independent calculation uses direct matrix powers and rational Lagrange interpolation. Finite exact checks show that all coefficients are positive for $3\leq n\leq12$ and that the linear coefficient is the only negative coefficient for $n=13$.

**Keywords:** Ehrhart polynomial; order polytope; polygon face lattice; exact computation; transfer matrix.

<a id="the-family-and-the-question"></a>

## 1 The family and the question

For a finite poset $R$, use the increasing-coordinate convention 

$$
\mathcal O(R)=\{x\in[0,1]^R:x_u\leq x_v\text{ whenever }u\leq_Rv\}.
$$

 This is a lattice polytope of dimension $|R|$. Indeed, its vertices are characteristic vectors of upper sets, and a linear extension gives a full-dimensional simplex inside it; see \[[2](#ref-Stanley)\]. Its Ehrhart polynomial is 

$$
E_R(t)=|t\mathcal O(R)\cap\mathbb Z^R|\quad(t\in\mathbb Z_{\geq0}),
$$

 which has degree $|R|$. A polytope is *Ehrhart-nonnegative* when every coefficient of this polynomial in the monomial basis is nonnegative.

Let $P_n$ be any convex polygon with $n\geq3$ vertices. Its full face lattice $\mathcal L(P_n)$ consists of a minimum $\hat0$, $n$ vertices, $n$ edges, and a maximum $\hat1$. Set 

$$
Q_n=\mathcal O(\mathcal L(P_n)),\qquad E_n=E_{\mathcal L(P_n)}.
$$

 In particular, $\dim Q_n=2n+2$. The geometry of the polygon does not affect this construction: its combinatorial face lattice depends only on $n$.

Lundström and Saud Maia Leite ask whether every $Q_n$ is Ehrhart-nonnegative \[[1](#ref-LSML)\]. The question is numbered 6.5 in their latest inspected preprint, version 5 dated 1 October 2026, and 6.4 in the published article. It concerns the *full* face lattice. Removing the minimum and maximum changes the counting polynomial. In particular, the circular-fence order-polynomial nonnegativity theorem of Ferroni, Morales and Panova \[[5](#ref-FMP), arXiv v3, Theorem 7.7\] concerns the crown itself and does not answer the full-face-lattice question.

<a id="thm:negative"></a>

**Theorem 1**. The polytope $Q_{13}$ has dimension $28$ and its Ehrhart polynomial satisfies <a id="eq:answer"></a>

$$
\boxed{[t]E_{13}(t)=-\frac{298495711}{35302608}<0.}
$$

**Equation (1)**

Consequently, the family $Q_n$ is not Ehrhart-nonnegative for all $n\geq3$.

The contribution is the exact counterexample in this specified family and the finite minimality check below; the counting framework and polynomial-recovery tools are established.

Negative coefficients for order polytopes in general are already known; for example, Liu and Tsuchiya analyze such families in \[[3](#ref-LT)\]. The claim here is confined to the specific polygon face-lattice question. The exact arithmetic and the source’s dated open-question statement do not by themselves establish priority over every intervening or unpublished result.

<a id="a-transfer-matrix-counting-formula"></a>

## 2 A transfer-matrix counting formula

The proper nonempty faces form the crown poset with minimal elements $a_1,\ldots,a_n$ and maximal elements $b_1,\ldots,b_n$, with relations 

$$
a_i<b_i,\qquad a_{i+1}<b_i,
$$

 where indices are cyclic. Let $C_n(m)$ count its order-preserving maps into $\{0,\ldots,m\}$.

The crown trace identity below is the alternating specialization of Huang’s circular-fence transfer formula \[[4](#ref-Huang), Proposition 4.1\]: its lower- and upper-triangular $0$–$1$ transfer matrices multiply to $K_N=(\min(i,j))$. A direct derivation is included to make the coefficient certificate self-contained.

<a id="lem:count"></a>

**Lemma 2**. For $N\geq1$, put $K_N=(\min(i,j))_{i,j=1}^N$. Then <a id="eq:crown"></a><a id="eq:full"></a>

$$
\begin{aligned}
 C_n(m)&=\operatorname{tr}(K_{m+1}^{\,n}),\\
 E_n(m)&=\sum_{k=0}^m(m-k+1)\operatorname{tr}(K_{k+1}^{\,n})\qquad(m\geq0).
\end{aligned}
$$

**Equations (2), (3)**

*Proof.* Fix values $x_i\in\{0,\ldots,m\}$ on $a_i$. The coordinate on $b_i$ can be chosen independently in $m+1-\max(x_i,x_{i+1})$ ways. Therefore 

$$
C_n(m)=\sum_{x_1,\ldots,x_n=0}^m
 \prod_{i=1}^n\bigl(m+1-\max(x_i,x_{i+1})\bigr),\qquad x_{n+1}=x_1.
$$

 This is the trace of the $n$th power of the matrix with entries $m+1-\max(x,y)$, indexed by $0\leq x,y\leq m$. Reversing the row and column order gives $K_{m+1}$, proving [(2)](#eq:crown).

For the full face lattice, fix coordinates $u\leq v$ on $\hat0,\hat1$. All crown coordinates lie between them. If $k=v-u$, subtracting $u$ gives $C_n(k)$ assignments. For each $k$, there are exactly $m-k+1$ pairs $(u,v)$ with $0\leq u\leq v\leq m$ and difference $k$. Summing proves [(3)](#eq:full). ◻

The direct count also realizes the standard twofold lattice-pyramid construction and its Ehrhart-series transformation; see \[[1](#ref-LSML), arXiv v5, Proposition 6.1 and Theorem 6.6\]. In particular, it gives the series identity <a id="eq:series"></a>

$$
\sum_{m\geq0}E_n(m)z^m=\frac{1}{(1-z)^2}\sum_{m\geq0}C_n(m)z^m.
$$

**Equation (4)**

<a id="an-integer-recurrence-and-a-compact-certificate"></a>

## 3 An integer recurrence and a compact certificate

<a id="lem:det"></a>

**Lemma 3**. For $N\geq0$, with an empty determinant interpreted as one, <a id="eq:det"></a>

$$
D_N(z):=\det(I-zK_N)=\sum_{j=0}^N(-z)^j\binom{N+j}{2j}.
$$

**Equation (5)**

*Proof.* Write $K_N=LL^{\mathsf T}$, where $L$ is the lower-triangular matrix whose entries on and below the diagonal are all one. Then $\det K_N=1$ and $K_N^{-1}$ is tridiagonal, with diagonal $2,\ldots,2,1$ and adjacent off-diagonal entries $-1$. Thus $D_N(z)=\det(K_N^{-1}-zI)$. Expanding this continuant at its first row gives 

$$
D_N=(2-z)D_{N-1}-D_{N-2},\qquad D_0=1,\quad D_1=1-z.
$$

 The coefficients on the right side of [(5)](#eq:det) satisfy these same initial conditions and recurrence, by Pascal’s identity. This proves the formula by induction. ◻

Set $e_j(N)=\binom{N+j}{2j}$ when $0\leq j\leq N$, and set it to zero otherwise. Newton’s identities applied to [(5)](#eq:det) give, for $r\geq1$, <a id="eq:newton"></a>

$$
T_r(N):=\operatorname{tr}(K_N^r)=\sum_{j=1}^{r-1}(-1)^{j-1}e_j(N)T_{r-j}(N)
 +(-1)^{r-1}r e_r(N).
$$

**Equation (6)**

All arithmetic here is integral. Thus either direct matrix multiplication or this recurrence determines every count in [(3)](#eq:full) exactly.

For $n=13$, the crown has dimension $26$. Write its Ehrhart series as $h^*(z)/(1-z)^{27}$. The coefficients of its numerator are <a id="eq:h"></a>

$$
h_j=\sum_{r=0}^j(-1)^r\binom{27}{r}T_{13}(j-r+1),\qquad 0\leq j\leq26.
$$

**Equation (7)**

Using [(6)](#eq:newton) in [(7)](#eq:h) gives $h_{25}=h_{26}=0$ and $h_j=h_{24-j}$ for $0\leq j\leq24$. The following half-table therefore specifies the entire numerator:

| $j$ |                 $h_j$ |
|----:|----------------------:|
|   0 |                     1 |
|   1 |                271416 |
|   2 |            1378078419 |
|   3 |          837258390856 |
|   4 |       131296310558015 |
|   5 |      7724454986455746 |
|   6 |    209821561170879574 |
|   7 |   2985931198521851042 |
|   8 |  24154691761269157097 |
|   9 | 117280290847971630454 |
|  10 | 354406898580482272679 |
|  11 | 682213052793220234662 |
|  12 | 847462155807564227086 |

The symmetry in this table is verified by the recurrence; it need not be assumed as an input.

Equation [(4)](#eq:series) preserves the numerator and changes the denominator to $(1-z)^{29}$. Consequently <a id="eq:binomial"></a>

$$
E_{13}(t)=\sum_{j=0}^{24}h_j\binom{t+28-j}{28},
$$

**Equation (8)**

where the binomial symbols denote polynomials. If $1\leq j\leq28$, exactly one factor of $\binom{t+28-j}{28}$ vanishes at $t=0$, so 

$$
[t]\binom{t+28-j}{28}=\frac{(-1)^{j-1}(j-1)!(28-j)!}{28!}
 =\frac{(-1)^{j-1}}{j\binom{28}{j}}.
$$

 The term with $j=0$ has linear coefficient $H_{28}=\sum_{r=1}^{28}1/r$. Thus [(8)](#eq:binomial) and the displayed integers prove <a id="eq:linearh"></a>

$$
[t]E_{13}(t)=H_{28}+\sum_{j=1}^{24}\frac{(-1)^{j-1}h_j}{j\binom{28}{j}}
 =-\frac{298495711}{35302608},
$$

**Equation (9)**

which completes the proof of Theorem [1](#thm:negative).

<a id="sec:independent"></a>

## 4 A second exact route and finite minimality

The following coefficient identity provides an independent certificate, without the determinant formula or Ehrhart numerator.

<a id="lem:lagrange"></a>

**Lemma 4**. If $f$ is a polynomial of degree at most $d$, then <a id="eq:lagrange"></a>

$$
[t]f(t)=-H_df(0)+\sum_{j=1}^d\frac{(-1)^{j-1}}{j}\binom dj f(j).
$$

**Equation (10)**

*Proof.* Use the Lagrange interpolation basis on $0,1,\ldots,d$. The basis element at zero is $\prod_{k=1}^d(1-t/k)$, whose derivative at zero is $-H_d$. For $j>0$, differentiating its unique factor $t$ gives derivative $(-1)^{j-1}\binom dj/j$. Summing these derivatives times the interpolation values proves the assertion. ◻

Compute $E_{13}(0),\ldots,E_{13}(28)$ from [(3)](#eq:full), using direct integer matrix products. With $D=\operatorname{lcm}(1,\ldots,28)=80313433200$, the resulting integer identity is <a id="eq:integer"></a>

$$
-\sum_{j=1}^{28}\frac Dj+
 \sum_{j=1}^{28}(-1)^{j-1}\binom{28}{j}\frac Dj E_{13}(j)
 =-679077742525.
$$

**Equation (11)**

Here $E_{13}(0)=1$; for scale, $E_{13}(1)=271445$ and $E_{13}(28)=3587915312358916716605780580224674$. Dividing [(11)](#eq:integer) by $D$ and reducing gives [(1)](#eq:answer) exactly. All 29 values, the full rational polynomial, and the direct-matrix verifier are supplied in the reproducibility package.

<a id="prop:minimal"></a>

**Proposition 5** (Finite exact coefficient check). For every $3\leq n\leq12$, all coefficients of $E_n(t)$ are strictly positive. For $n=13$, the linear coefficient is the only negative coefficient; all other coefficients are strictly positive. In particular, $13$ is the least polygon size yielding a counterexample in this family.

*Computer-assisted proof.* For each of the eleven integers $n=3,\ldots,13$, formula [(3)](#eq:full) determines $2n+3$ integer values, which determine $E_n$ because its degree is $2n+2$. The included standard-library verifier computes these values by [(6)](#eq:newton), expands the Newton interpolation basis with exact rational arithmetic, and checks the sign of every coefficient. Its second implementation uses direct matrix powers and the full Lagrange basis with exact rational coefficients; it obtains the same polynomials and signs. The resulting full coefficient vectors are included as machine-readable rational numbers. The proof is this finite exact calculation, not a numerical tolerance test or an inference from sampled evaluations. ◻

The second implementation also checks full coordinate enumeration in seven small cases, agrees at three additional evaluation points beyond each interpolation range, and verifies the zeros at $-1,-2,-3,-4$ and the symmetry $E_n(-5-t)=E_n(t)$. For $n=7$, it reproduces the order-polynomial linear coefficient $[t]\Omega_{\mathcal L(P_7)}(t)=-3/1430$ discussed in \[[1](#ref-LSML)\], with $\Omega_{\mathcal L(P_n)}(t)=E_n(t-1)$. This last distinction prevents confusion between the order-polynomial and Ehrhart-polynomial linear coefficients.

<a id="an-optional-real-root-certificate-at-the-counterexample-size"></a>

## 5 An optional real-root certificate at the counterexample size

The negative Ehrhart coefficient does not come from a non-real-rooted numerator. The same integer table gives 

$$
h^*(z)=(1+z)^{24}\Gamma\!\left(\frac{z}{(1+z)^2}\right),
$$

 where the coefficients of the degree-twelve polynomial $\Gamma$, in ascending order, are 

$$
\begin{aligned}
 (&1,\ 271392,\ 1372107519,\ 809753546900,\\
  &116459628330899,\ 5735642452639018,\ 114879997532053963,\\
  &1017711233823543432,\ 4088778012033034128,\\
  &7234249303551155456,\ 5083364114942823680,\\
  &1097874694239193088,\ 31241944868450304).
\end{aligned}
$$

 Exact rational substitution gives opposite signs at the endpoints of each of these twelve disjoint open intervals: 

$$
\begin{gathered}
(-30,-29),\quad(-4,-3),\quad(-2,-1),\\
(-1/2,-1/3),\quad(-1/4,-1/5),\quad(-1/8,-1/9),\\
(-1/17,-1/18),\quad(-1/39,-1/40),\quad(-1/111,-1/112),\\
(-1/472,-1/473),\quad(-1/4485,-1/4486),\quad(-1/4486,0).
\end{gathered}
$$

 The intermediate value theorem gives twelve distinct negative roots, accounting for the entire degree. For each $y<0$, the equation $y(1+z)^2=z$ has two distinct negative real roots: its discriminant is $1-4y>0$, its root product is one, and its root sum is $(1-2y)/y<0$. Different $y$ give disjoint pairs. It follows that $h^*$ has 24 distinct negative real roots. The accompanying certificate verifies the polynomial identity and every endpoint sign using fractions.

This supplementary calculation concerns $n=13$ and makes no all-size real-rootedness assertion. The general coexistence of a real-rooted $h^*$-polynomial and negative Ehrhart coefficients is already exhibited by the Eulerian-product examples in \[[3](#ref-LT), Example 3.2\]; no novelty claim is made for that broader phenomenon.

<a id="reproducibility-and-limitations"></a>

## 6 Reproducibility and limitations

The package contains two independent arithmetic implementations, the full coefficient data, this LaTeX source, and build and verification instructions. The principal verifier needs only Python’s standard library. It checks the half-table, the exact negative coefficient, all signs in Proposition [5](#prop:minimal), and the optional real-root certificate. The direct-matrix implementation is slower but does not use the determinant recurrence or Newton interpolation.

The numerical assertions use integer or rational arithmetic throughout. Both extremal faces are included in the poset convention; the verification code implements exactly the counting formulas stated above. The finite coefficient checks do not assert a pattern of positivity or negativity for all larger $n$.

Question 6.5 is posed in the preprint version of 1 October 2026 \[[1](#ref-LSML)\]. The transfer and pyramid framework is established prior work. The result here is the exact counterexample and the stated finite minimality within this family; no dimension-minimality claim among all posets is made.

## References

<a id="ref-LSML"></a>

**\[1\]**

T. Lundström and L. Saud Maia Leite, *Order polytopes of crown posets*, European Journal of Combinatorics **133** (2026), 104304. [doi:10.1016/j.ejc.2025.104304](https://doi.org/10.1016/j.ejc.2025.104304). Updated preprint: [arXiv:2504.05123v5](https://arxiv.org/abs/2504.05123v5), 1 October 2026.

<a id="ref-Stanley"></a>

**\[2\]**

R. P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry **1** (1986), 9–23. [Author-hosted paper](https://math.mit.edu/~rstan/pubs/pubfiles/66.pdf).

<a id="ref-LT"></a>

**\[3\]**

F. Liu and A. Tsuchiya, *Stanley’s non-Ehrhart-positive order polytopes*, Advances in Applied Mathematics **108** (2019), 1–10. [doi:10.1016/j.aam.2019.03.004](https://doi.org/10.1016/j.aam.2019.03.004). [arXiv:1806.08403](https://arxiv.org/abs/1806.08403).

<a id="ref-Huang"></a>

**\[4\]**

P. C. Huang, *Bernstein Transfers and Greedy Records for Fence and Circular-Fence Order Polynomials*, [arXiv:2607.22767v2](https://arxiv.org/abs/2607.22767v2), 31 July 2026.

<a id="ref-FMP"></a>

**\[5\]**

L. Ferroni, A. H. Morales and G. Panova, *Skew shapes, Ehrhart positivity and beyond*, Proceedings of the London Mathematical Society **133**(2) (2026), e70204. [doi:10.1112/plms.70204](https://doi.org/10.1112/plms.70204). Preprint: [arXiv:2503.16403v3](https://arxiv.org/abs/2503.16403v3), 28 July 2026.
