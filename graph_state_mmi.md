# Monogamy of Mutual Information and Claw Vertex Minors in Qubit Graph States

Mantra Patel

10 October 2026

## Abstract

A qubit graph state violating monogamy of mutual information (MMI) has a local-Clifford graph representative containing an induced claw. A finite-certificate proof first classifies graphs with no claw vertex minor: each connected component is locally equivalent, up to isomorphism, to one of $K_1,K_2,P_3,P_4,C_5,W_5$, where $W_5$ is the six-vertex wheel. All six representatives obey monogamy of mutual information for every subsystem choice. The argument proves the one-way forbidden-subgraph assertion in Conjecture 1 of arXiv:2511.19585v1, without making claw presence sufficient for violation. Separately, a five-type finite-state argument and an exact alternating-cycle correction establish MMI for every graph of maximum degree at most two. The five-vertex path demonstrates that these MMI families extend beyond claw-vertex-minor exclusion. The proofs are accompanied by exact extension and orbit certificates and separately implemented computational checks.

**Keywords:** graph states; monogamy of mutual information; vertex minors; cut rank; finite certificates.

<a id="statement-and-context"></a>

## 1 Statement and context

Let $G=(V,E)$ be a finite simple graph. Its graph state is 

$$
|G\rangle=\prod_{\{u,v\}\in E}\mathrm{CZ}_{uv}|+\rangle^{\otimes |V|}.
$$

 For $X\subseteq V$, write $S(X)$ for the von Neumann entropy, in bits, of the reduced state on $X$. For pairwise-disjoint $A,B,C\subseteq V$, define <a id="eq:I3"></a>

$$
I_3(A:B:C)=S(A)+S(B)+S(C)+S(ABC)-S(AB)-S(AC)-S(BC),
$$

**Equation (1)**

where juxtaposition denotes union. Monogamy of mutual information (MMI) is the assertion $I_3\leq0$.

Fuentes, Keeler, Munizzi and Pollack conjecture that any graph state violating some MMI inequality has a local-Clifford representative containing a four-vertex star \[[1](#ref-FKMP), Conjecture 1, manuscript p. 30\]. Their notation $K_4$ denotes that star; here it is called the *claw* $K_{1,3}$, avoiding confusion with the complete graph. The first result proves this necessary condition.

<a id="thm:claw"></a>

**Theorem 1**. If the qubit graph state of a finite simple graph $G$ has $I_3(A:B:C)>0$ for some pairwise-disjoint vertex sets, then a sequence of local complementations transforms $G$ into a graph containing an induced claw. In particular, a local-Clifford representative has the generalized-star partition required by Conjecture 1 of \[[1](#ref-FKMP)\].

The proof uses an exact finite classification of claw-vertex-minor-free connected graphs, followed by elementary entropy calculations. It is a computer-assisted finite-certificate proof with an explicit all-size induction. It does not characterize all MMI states. The necessary condition holds for every connected graph on at least seven vertices, irrespective of its MMI behavior, and its converse already fails for $P_5$.

Observation 9 of \[[1](#ref-FKMP)\] separately reports MMI for paths and cycles through ten vertices. The second result establishes this family property at every size, including arbitrarily disconnected subsystems.

The cut-rank description of graph-state entanglement is established background \[[2](#ref-Hein2004); [3](#ref-Hein2006)\]. A separate related framework is that of weighted terminal-min-cut graph entropies: Bao et al. identify their cone with the holographic entropy cone and give a graph-model proof of MMI \[[4](#ref-Bao), Definition 2, Theorem 5 and Section 4.1\]. An ordinary graph-state adjacency graph should not be identified with such a graph model without a separate entropy-preserving construction. The present proof instead works directly with binary cut ranks and retains an explicit treatment of the fully alternating even-cycle exception.

<a id="thm:main"></a>

**Theorem 2**. If $G$ has maximum degree at most two, then its graph state satisfies $I_3(A:B:C)\leq0$ for all pairwise-disjoint $A,B,C\subseteq V$. The same assertion holds for every state $\bigotimes_{v\in V}U_v|G\rangle$, where each $U_v$ is a single-qubit unitary.

The degree-two proof is analytic and finite-state. The classification proof explicitly uses a finite exact certificate and orbit-closure verification; its all-size conclusion follows by induction rather than extrapolation from small graphs. The exact computational cross-checks are described in Section [9](#sec:checks); related work and the scope of the conclusions are discussed in Section [10](#sec:scope).

<a id="entropy-as-cut-rank"></a>

## 2 Entropy as cut rank

Put $D=V\setminus(A\cup B\cup C)$. Purity gives $S(ABC)=S(D)$ and $S(BC)=S(AD)$. Thus <a id="eq:seven"></a>

$$
I_3=\sum_{X\in\mathcal C}c_X S(X),\qquad
 \mathcal C=(A,B,C,D,AB,AC,AD),\qquad c=(1,1,1,1,-1,-1,-1).
$$

**Equation (2)**

These are the seven cuts of four colors, up to complementation.

For completeness, the standard graph-state cut-rank identity can be derived directly. Let $\Gamma$ be the adjacency matrix of $G$, regarded over $\mathbb F_2$. The graph state is stabilized by $K_v=X_v\prod_{w\sim v}Z_w$. A stabilizer product indexed by a binary vector supported on $X$ is supported entirely in $X$ precisely when its vector lies in the kernel of $\Gamma_{V\setminus X,X}$. Hence the subgroup supported in $X$ has binary dimension $|X|-r$, where $r=\operatorname{rank}_{\mathbb F_2}\Gamma_{X,V\setminus X}$. The reduced density operator is the normalized projector onto the common $+1$ eigenspace of this subgroup, a space of dimension $2^r$. Therefore <a id="eq:rank"></a>

$$
S(X)=\operatorname{rank}_{\mathbb F_2}\Gamma_{X,V\setminus X}.
$$

**Equation (3)**

For the foundational formulation, see \[[3](#ref-Hein2006), Proposition 10, equation (132), and the flat-spectrum discussion leading to equation (161)\], as well as \[[2](#ref-Hein2004)\]. It is also restated as equation (2.19) of \[[1](#ref-FKMP)\]; the derivation here is included for completeness.

<a id="sec:classification"></a>

## 3 Graphs without a claw vertex minor

A *local complementation* at a vertex $v$, denoted $G*v$, toggles every edge between two distinct neighbors of $v$ and leaves all other edges unchanged. Graphs obtainable from one another by these operations are locally equivalent. A *vertex minor* is obtained by local complementations and vertex deletions. We use $\mathcal Q$ for the class of graphs with no claw $K_{1,3}$ as a vertex minor.

Local complementation is implemented on graph states by a product of single-qubit Clifford unitaries \[[3](#ref-Hein2006)\]. Consequently it preserves every subsystem entropy. The graph-theoretic terminology and standard framework are reviewed in \[[5](#ref-KimOum)\]; the elementary closure properties needed here are proved next.

<a id="lem:closure"></a>

**Lemma 3**. A graph belongs to $\mathcal Q$ if and only if no graph in its local-complementation orbit has an induced claw. The class $\mathcal Q$ is inherited by induced subgraphs. Local complementation preserves connected components.

*Proof.* If $v\in U$, then $(G*v)[U]=G[U]*v$. Thus a sequence using only vertices of $U$ can be lifted to $G$, with precisely the same induced graph on $U$. Intermediate deletions in a vertex-minor sequence can therefore be postponed until its end: no subsequently complemented vertex was deleted earlier. This proves the equivalence and induced-subgraph inheritance.

A local complementation cannot introduce an edge between distinct connected components. If it removes an edge $xy$, both endpoints are neighbors of the complemented vertex $v$, so the unchanged edges $xv$ and $vy$ still join them. Connectivity within a component is therefore preserved. ◻

For $1\leq k\leq6$, define fixed labeled representatives <a id="eq:reps"></a>

$$
R_1=K_1,\quad R_2=K_2,\quad R_3=P_3,\quad R_4=P_4,\quad R_5=C_5,\quad R_6=W_5.
$$

**Equation (4)**

Here $W_5$ means a five-cycle with an additional universal hub, hence has six vertices. For $k\leq4$, the vertices are $0,\ldots,k-1$ and edges are $i(i+1)$. The cycle $R_5$ has edges $01,12,23,34,40$. In $R_6$, vertex $5$ is adjacent to all five rim vertices.

<a id="lem:extension"></a>

**Lemma 4** (Finite extension lemma). For every $1\leq k\leq6$, attach a new vertex $k$ to a nonempty subset of $V(R_k)$. The resulting graph either has an induced claw after a specified sequence of local complementations, or is locally equivalent up to relabeling to $R_{k+1}$. The latter outcome is possible only when $k<6$.

*Finite-certificate proof.* There are $\sum_{k=1}^6(2^k-1)=120$ attachments. Their exact certificate gives the following exhaustive counts:

| Base  | Attachments | Claw outcome | Next representative |
|:-----:|------------:|-------------:|--------------------:|
| $R_1$ |           1 |            0 |                   1 |
| $R_2$ |           3 |            0 |                   3 |
| $R_3$ |           7 |            1 |                   6 |
| $R_4$ |          15 |           11 |                   4 |
| $R_5$ |          31 |           30 |                   1 |
| $R_6$ |          63 |           63 |                   0 |

Appendix [A](#app:extensions) displays a symmetry-reduced certificate. Path reversal covers $R_1,\ldots,R_4$; the dihedral symmetries of the rim cover $R_5$. The listed mask orbits partition all nonempty neighborhoods for these five bases. Each row is checked by toggling the indicated neighbor pairs and testing the resulting four-vertex claw or the displayed representative permutation.

For $R_6$, a new vertex with a nonempty proper subset of rim neighbors has a claw witness already in its restriction to the rim and the new vertex, by the $R_5$ rows. This covers $60$ attachments, independently of adjacency to the old hub. The remaining three attachments, with new vertex $6$, are 

$$
\begin{array}{c|c|c}
N(6)&\text{LC word}&\text{claw }(\text{center};\text{leaves})\\\hline
\{5\}&()&(5;0,2,6)\\
\{0,1,2,3,4\}&(0,2)&(0;4,5,6)\\
\{0,1,2,3,4,5\}&(0)&(0;1,5,6).
\end{array}
$$

 These witnesses are checked directly. Thus the finite table proves the lemma. All claw witnesses in the full certificate use at most two complementations. A reduction to the next representative, for $R_3$ with new neighborhood $\{0,2\}$, uses three; no two-operation bound is claimed for every row. ◻

<a id="thm:class"></a>

**Theorem 5** (Claw vertex-minor exclusion). A finite simple graph has no claw vertex minor if and only if each connected component is locally equivalent, up to isomorphism, to one of the six graphs in [(4)](#eq:reps). In particular, every connected graph on at least seven vertices has a claw vertex minor.

*Proof.* First prove necessity for a connected $k$-vertex graph in $\mathcal Q$, by induction for $k\leq6$. The case $k=1$ is immediate. Any connected graph with at least two vertices has a vertex $v$ whose deletion leaves it connected: take a leaf of a spanning tree. By Lemma [3](#lem:closure), $G-v$ belongs to $\mathcal Q$, so it is locally equivalent up to isomorphism to $R_{k-1}$. Lift that sequence to $G$ and extend the relabeling to $v$. The resulting graph is connected and restricts to $R_{k-1}$, hence is a nonempty attachment covered by Lemma [4](#lem:extension). Its claw outcome is impossible, so the next representative is $R_k$.

The same reasoning for $k=7$ would produce an attachment to $R_6$, but every such attachment has a claw witness. Thus no connected seven-vertex graph belongs to $\mathcal Q$. Repeated deletion of spanning-tree leaves produces a connected induced seven-vertex subgraph of any larger connected graph; induced-subgraph inheritance excludes those graphs as well.

For sufficiency, compute the complete labeled local-complementation orbits of the six fixed representatives by closure under complementing at every vertex. Their respective sizes are $1,1,4,11,132,132$. Every graph in each finite closure is directly claw-free. The accompanying independent checker verifies membership of the starting graph, closure under every generator, reachability through supplied local-complementation words, and claw absence. Thus each $R_k$ belongs to $\mathcal Q$. This is an exact finite part of the proof, not an inference from the displayed counts alone. Local complementation cannot mix connected components, so the equivalence extends to their disjoint unions. ◻

<a id="sec:claw-mmi"></a>

## 4 The necessary claw condition for MMI failure

It remains to evaluate MMI on the six representatives. If a four-part partition has an empty part, purity gives $I_3=0$. Thus $R_1,R_2,R_3$ require no further calculation. For $P_4$, four nonempty parts are singletons: their entropy sum is four, while the three inequivalent pair cuts have ranks $1,2,2$. Hence $I_3=-1$.

For $C_5$, every cut satisfies $S(X)=\min(|X|,5-|X|)$. It suffices to check two-vertex cuts: both rows of their crossing matrix are nonzero and unequal, hence independent over $\mathbb F_2$. Singleton ranks follow by connectivity and larger cuts by complementation. A nonempty four-part partition has sizes $(2,1,1,1)$, so the positive entropy sum is five and each pair cut has rank two. Again $I_3=-1$.

For $W_5$, every cut satisfies $S(X)=\min(|X|,6-|X|)$. Here is a short direct check rather than an appeal to an absolutely maximally entangled-state classification. Up to the rim’s dihedral action, the three-vertex sets have representatives and cut matrices 

$$
\begin{array}{c|c@{\qquad}c|c}
X&\Gamma_{X,X^c}&X&\Gamma_{X,X^c}\\\hline
\{0,1,2\}&\begin{pmatrix}0&1&1\\0&0&1\\1&0&1\end{pmatrix}&
\{0,1,3\}&\begin{pmatrix}0&1&1\\1&0&1\\1&1&1\end{pmatrix}\\[10pt]
\{0,1,5\}&\begin{pmatrix}0&0&1\\1&0&0\\1&1&1\end{pmatrix}&
\{0,2,5\}&\begin{pmatrix}1&0&1\\1&1&0\\1&1&1\end{pmatrix}.
\end{array}
$$

 Rows and columns are in increasing vertex order. Every displayed determinant is one over $\mathbb F_2$. Every two-vertex cut is also independent: extend its vertices to a triple, whose three rows are independent on the smaller complementary column set. The two selected rows remain independent when additional complementary columns are restored. Singleton cuts have rank one, and other cuts follow by complementation.

The possible nonempty four-part size patterns for $W_5$ are $(3,1,1,1)$ and $(2,2,1,1)$. Their positive entropy sums are six and their pair-cut sums are respectively six and eight. Therefore $I_3$ is respectively zero and $-2$. All six representatives satisfy every MMI inequality.

*Proof of Theorem [1](#thm:claw).* If $G$ has no claw vertex minor, Theorem [5](#thm:class) places every connected component in one of the six locally equivalent families just checked. Local Clifford operations preserve the entropies, and graph-state tensor factors over connected components make $I_3$ additive. Thus every partition of $G$ has $I_3\leq0$. Contraposition proves the theorem. ◻

To recover the generalized-star formulation of \[[1](#ref-FKMP), Conjecture 1\], take an induced claw in the resulting graph $H$, put its three leaves in separate singleton parts $I,J,K$, and put all remaining vertices, including the claw center, in a central part $Z$. There are no edges between $I,J,K$, and each is anchored to $Z$ by its edge to the claw center. This is precisely the multi-vertex-center construction of \[[1](#ref-FKMP), Section 4.2\]; it imposes no assertion that this particular partition violates MMI. The existence of a star-shaped partition and the location of an MMI violation are distinct statements.

<a id="the-converse-fails."></a>

##### The converse fails.

Let $P_5$ have edges $01,12,23,34$. Complementing successively at vertices $1$ and $2$ produces an induced claw on $\{0,1,3,4\}$, with center $3$. Nevertheless, Theorem [2](#thm:main) shows that $P_5$ obeys every MMI inequality. Thus claw presence is not sufficient for MMI failure. Moreover, Theorem [5](#thm:class) makes the necessary condition automatic for any graph with a connected component of order at least seven. The necessary condition is consequently weak on large connected graphs and is not a classification of MMI-satisfying states.

<a id="path-cut-ranks"></a>

## 5 Path cut ranks

The *crossing graph* of $X$ retains only edges between $X$ and its complement. For a path, every nontrivial crossing component is a path.

<a id="lem:pathrank"></a>

**Lemma 6**. The binary biadjacency matrix of a path with $\ell$ edges has rank $\lceil\ell/2\rceil$. Consequently, a path cut has entropy equal to the sum of $\lceil\ell/2\rceil$ over its maximal crossing-edge runs.

*Proof.* Every nonzero minor of size $k$ supplies a matching of size $k$, because any nonzero determinant term selects $k$ disjoint edges. Thus rank is at most the maximum matching size. Conversely, take a maximum matching of a forest and the square submatrix on its endpoints. The induced forest has this matching as a perfect matching and cannot have another: the symmetric difference of two distinct perfect matchings contains a cycle. The corresponding determinant therefore has exactly one nonzero term, so it is nonzero even over $\mathbb F_2$. The maximum matching size of an $\ell$-edge path is $\lceil\ell/2\rceil$. Ranks add over disjoint components. ◻

<a id="a-finite-state-proof-for-paths"></a>

## 6 A finite-state proof for paths

Color the path vertices by the part $A,B,C,D$ containing them. After scanning an initial segment of edges, let $q_X\in\{0,1\}$ be the parity of the current crossing run for cut $X$; a noncrossing last edge sets $q_X=0$. Initially $q=0$. Appending an edge from color $a$ to color $b$ updates <a id="eq:update"></a>

$$
q'=e(a,b)\mathbin{\wedge}\neg q,\qquad
 e(a,b)_X=\mathbf1\{X\text{ separates }a\text{ and }b\}.
$$

**Equation (5)**

Here conjunction and negation act coordinatewise. The rank increment for cut $X$ is $q'_X$: the first, third, and later odd-numbered edges in a crossing run contribute one. Thus the increment in $I_3$ is 

$$
w(q')=\sum_{X\in\mathcal C}c_Xq'_X.
$$

 The last color $a$ is included in the scan state.

When $a=b$, $e(a,b)=0$. Otherwise this vector has the two singleton bits $a,b$ and two of the three pair-cut bits. There are only five structural types to consider:

| Type  | Nonzero bits of $q$ when last color is $a$ | Potential $p$ |
|:-----:|:-------------------------------------------|:-------------:|
|  $Z$  | None                                       |      $0$      |
|  $E$  | The bits of $e(a,b)$ for some $b\ne a$     |      $0$      |
| $S_0$ | Singleton $a$ only                         |      $0$      |
| $S_1$ | Singleton $a$ and one pair-cut bit         |      $0$      |
| $S_2$ | Singleton $a$ and two pair-cut bits        |     $-1$      |

Every state reached from an initial state belongs to this list. The complete structural transition possibilities are <a id="eq:table"></a>

$$
\begin{array}{c|l}
\text{Source}&\text{Target types with their increments}\\\hline
Z& Z\ (0),\ E\ (0)\\
E& Z\ (0),\ S_1\ (0)\\
S_0& Z\ (0),\ S_2\ (-1)\\
S_1& Z\ (0),\ S_1\ (0),\ S_2\ (-1)\\
S_2& Z\ (0),\ S_1\ (0),\ S_0\ (+1).
\end{array}
$$

**Equation (6)**

Here a type-level possibility need not occur for every particular labeled state; the table contains all possibilities and is sufficient for the induction.

To verify it, consider an appended color $b\ne a$. For an $S_j$ state, the update removes the old singleton bit $a$ and leaves exactly singleton $b$. Of the two pair bits in $e(a,b)$, the bits already present in $q$ are removed. If $j=0$, two remain; if $j=1$, one or two remain; if $j=2$, zero or one remains, since two two-element subsets of a three-element set intersect. The corresponding weight is one minus the number of surviving pair bits. For an $E$ state, returning to its other endpoint gives $Z$; choosing a third color leaves one singleton and one pair bit. Repeating color $a$ always gives $Z$. This proves both closure of the five types and the table.

<a id="prop:path"></a>

**Proposition 7**. Every path graph state satisfies MMI for every four-color partition.

*Proof.* For every transition in [(6)](#eq:table), direct inspection gives <a id="eq:potential"></a>

$$
w(q')\leq p(q')-p(q).
$$

**Equation (7)**

The initial potential is zero and every final potential is nonpositive. Summing [(7)](#eq:potential) over the path proves $I_3\leq p(q_{\mathrm{final}})\leq0$. ◻

The same table yields an exact equality test. A negative increment occurs exactly on entry to $S_2$, and a positive increment exactly on $S_2\to S_0$. Therefore $I_3$ is minus the number of visits to $S_2$ that are not immediately followed by $S_0$, counting a terminal visit as unpaired. This is a consequence of the same theorem, not a separate open-problem resolution.

<a id="cycles-and-the-alternating-cut-exception"></a>

## 7 Cycles and the alternating-cut exception

Let $G=C_n$, $n\geq3$. If one of $A,B,C,D$ is empty, purity makes [(1)](#eq:I3) zero. Assume henceforth that all four colors occur.

A cut with a noncrossing edge again has only path components and obeys Lemma [6](#lem:pathrank). If all edges cross, the cycle length is even, say $n=2m$, and its biadjacency matrix is $I+P$, where $P$ is a cyclic permutation matrix of size $m$. Its kernel consists of the constant vectors, so its rank is $m-1$. This includes $m=2$, where the matrix is the all-ones $2\times2$ matrix. A periodic parity scan counts $m$ for such a cut and therefore overcounts its entropy by exactly one. Call such a cut *fully alternating*.

<a id="lem:onecut"></a>

**Lemma 8**. If all four colors occur, at most one of the seven inequivalent cuts is fully alternating.

*Proof.* There are three cases for a pair of distinct cuts. If two singleton cuts are fully alternating, every edge must connect their two colors, excluding the other colors. If a singleton cut $a$ and a pair cut are fully alternating, complement the pair cut so it contains $a$, and write it as $ab\mid cd$. Every edge must then connect $a$ to $c$ or $d$, excluding $b$. Finally, two distinct pair cuts give four distinct two-bit signatures to the four colors. Each edge must connect complementary signatures. Connectedness forces the cycle to use only one such complementary pair. Each case contradicts occurrence of all four colors. ◻

<a id="no-alternating-cut-or-an-alternating-singleton-cut"></a>

### 7.1 No alternating cut or an alternating singleton cut

Start the path scan at any vertex and scan two copies of the cyclic word, including each closing edge. Every coordinate with a noncrossing edge resets in the first pass and has the same state at the end of each subsequent pass. A fully alternating coordinate also returns to its previous state after a pass, since $n$ is even. Thus after the first pass the scan follows a reachable periodic sequence of states. Its potential telescopes to zero around a full cycle, proving that its signed scan weight is nonpositive.

With no fully alternating cut, the scan weight equals $I_3$. With a fully alternating singleton cut, Lemma [8](#lem:onecut) shows this is the only entropy correction; its coefficient in [(2)](#eq:seven) is positive. Hence $I_3$ is the signed scan weight minus one, and is at most $-1$.

<a id="an-alternating-pair-cut"></a>

### 7.2 An alternating pair cut

Relabel the colors so the fully alternating cut is $AB\mid CD$. Each side has $m$ vertices, and both colors occur on each side. Every proper subset of the rows of $I+P$ is independent, because its only row dependency uses all rows; the same holds for columns. Accordingly, <a id="eq:singletons"></a>

$$
S(A)+S(B)+S(C)+S(D)=2m,\qquad S(AB)=m-1.
$$

**Equation (8)**

The cut $AC\mid BD$ has two disconnected bipartite blocks, consisting of edges of types $AD$ and $BC$. The cut $AD\mid BC$ similarly has blocks of types $AC$ and $BD$. Hence $S(AC)+S(AD)$ is the sum of the ranks of these four edge-type graphs.

Divide the cycle edges into maximal cyclic runs of one edge type, among $AC,AD,BC,BD$. No run is the whole cycle, since all four colors occur. These runs are precisely the nontrivial path components of the edge-type graphs. If $o$ is the number of runs of odd length, Lemma [6](#lem:pathrank) gives 

$$
S(AC)+S(AD)=\sum_{\text{runs}}\left\lceil\frac{\ell}{2}\right\rceil=m+\frac{o}{2}.
$$

 Substituting in [(2)](#eq:seven) yields the exact formula <a id="eq:cycleexact"></a>

$$
\boxed{I_3=1-\frac{o}{2}.}
$$

**Equation (9)**

The integer $o$ is even because the total edge count is even. It is nonzero: if every run had even length, all run-boundary vertices would lie on the same bipartition side. Each run would begin and end at the same actual color, so all these boundary vertices would share one color. Within each run, all vertices on that side have that same color. That side would therefore contain only one color, contradicting occurrence of both $A,B$ and both $C,D$. Thus $o\geq2$, and [(9)](#eq:cycleexact) proves MMI in the last case.

<a id="completion-of-the-degree-two-theorem"></a>

## 8 Completion of the degree-two theorem

Every finite simple graph of maximum degree at most two is a disjoint union of paths, isolated vertices, and cycles. Its graph state factors across connected components. Subsystem entropy, and therefore $I_3$, adds over those factors. Proposition [7](#prop:path) and the cycle argument imply the first assertion of Theorem [2](#thm:main).

For any subsystem $X$, a product of single-qubit unitaries factors as a unitary on $X$ and a unitary on its complement. It preserves the spectrum of the reduced density operator. All terms of $I_3$ are therefore unchanged. This proves the second assertion and in particular includes the local-Clifford orbit. No claim is made that a local-Clifford representative must itself have maximum degree two.

<a id="sec:checks"></a>

## 9 Exact certificates and computational validation

The claw-classification certificate covers all 120 nonempty one-vertex attachments to the six representatives exactly once. Each entry is checked by replaying its local complementations and then inspecting a claw or comparing with an explicit representative permutation. The independent matrix/set implementation also enumerates the 281 graphs in the six fixed labeled LC orbits, verifies claw absence and all cut entropies, and checks all $5{,}460$ four-color assignments of the representatives. These exhaustive finite checks support the finite lemmas; the connected-subgraph induction in Theorem [5](#thm:class) supplies the unbounded-size deduction. Appendix [A](#app:extensions) makes the attachment witnesses human-checkable.

The accompanying certificate lists all 44 reachable labeled scan states and 176 labeled transitions. Its potential takes value zero on 32 states and $-1$ on 12. Of the 176 inequalities [(7)](#eq:potential), 140 have slack zero and 36 have slack one. The certificate generator uses cuts $(A,B,C,ABC,AB,AC,BC)$, whose crossing indicators equal those of $(A,B,C,D,AB,AC,AD)$ by complementation.

A second implementation independently reconstructs the state graph, verifies the entire certificate, and evaluates entropies by binary Gaussian elimination. Its finite tests cover

- all $1{,}398{,}100$ four-colorings of paths with one through ten vertices;

- all $1{,}398{,}080$ four-colorings of cycles with three through ten vertices;

- $2{,}200$ seeded random paths, and $1{,}600$ seeded random cycles, at sizes up to $1{,}000$, including deliberately alternating singleton and pair cuts.

All tests pass. Cycle tests also verify the one-unit alternating-cut correction and formula [(9)](#eq:cycleexact). These tests check implementation consistency and expose small-case mistakes; the all-size conclusion rests on the proof above, not on extrapolation from these tests.

<a id="sec:scope"></a>

## 10 Scope and related work

The results establish the necessary claw condition of \[[1](#ref-FKMP), Conjecture 1\] and the all-size degree-two property of its Observation 9. The six-representative classification is a graph-theoretic statement; it is not a classification of all MMI states. Disjoint-union and local-unitary extensions, the path equality test, and the alternating-pair formula are consequences or components of this coherent analysis, not separate solved research problems.

There is substantial related structural prior work. Kwon and Oum explain that excluding a fixed star as a vertex minor bounds the order of a connected graph \[[6](#ref-KwonOum)\]. For connected graphs, the existence of an independent triple as a vertex minor is equivalent to the existence of a claw as a vertex minor. Indeed, a claw yields an independent triple by deleting its center. Conversely, postpone deletions to obtain a connected locally equivalent graph containing an independent triple. By \[[8](#ref-DabrowskiEtAl), arXiv v1, Lemma 7.7\], it contains an induced claw, $P_5$, or bull, each of which has a claw pivot minor \[[8](#ref-DabrowskiEtAl), arXiv v1, Proposition 7.8\]. Since an edge pivot is a sequence of three local complementations, the equivalence follows. Combining this observation with $R_{\mathrm{vm}}(3)=7$ from \[[7](#ref-Ascoli), Theorem 1.4 and Section 5\] gives the order-seven bound in Theorem [5](#thm:class). Thus that bound is also a consequence of earlier results. The proof above independently supplies an explicit six-representative classification with finite certificates, and its use for the MMI implication is treated separately.

The relation between the exact six-representative classification, earlier vertex-minor structure results, and the MMI implication warrants further comparison. The degree-two theorem is proved directly in terms of binary cut ranks; no entropy-preserving identification with a holographic graph model is assumed. The results do not provide a complete classification of MMI-satisfying graph states.

<a id="use-of-generative-ai"></a>

## Use of generative AI

OpenAI generative AI tools were used to help draft the manuscript.

<a id="data-availability"></a>

## Data availability

The mathematical certificates and verification code supporting the computational statements are supplied with the manuscript. The finite extension witnesses are also presented in Appendix [A](#app:extensions). No empirical or participant data are used.

<a id="app:extensions"></a>

## A A symmetry-reduced extension certificate

For base $R_k$, the new vertex is $k$ and a mask $m$ encodes its neighborhood: bit $i$ is one exactly when $i$ is a neighbor. Local-complementation words act from left to right. For a claw, the witness tuple lists its center followed by its leaves. For an $R_{k+1}$ outcome, the tuple is a permutation $p$ such that the transformed attachment equals the graph obtained by mapping old label $i$ of $R_{k+1}$ to $p_i$. The last column is the mask orbit under the path reversal or cycle dihedral symmetries specified in the text. Each listed row can therefore be transported to every mask in its orbit. The 24 rows below and the three explicit $R_6$ exceptions in Lemma [4](#lem:extension) suffice for all 120 attachments.

| Base  | $m$ |  LC word  | Outcome | Witness or permutation | Mask orbit       |
|:-----:|----:|:---------:|:--------|:-----------------------|:-----------------|
| Base  | $m$ |  LC word  | Outcome | Witness or permutation | Mask orbit       |
| $R_1$ |   1 |   $()$    | $R_2$   | $(0,1)$                | $1$              |
| $R_2$ |   1 |   $()$    | $R_3$   | $(1,0,2)$              | $1,2$            |
| $R_2$ |   3 |   $(1)$   | $R_3$   | $(0,1,2)$              | $3$              |
| $R_3$ |   1 |   $()$    | $R_4$   | $(2,1,0,3)$            | $1,4$            |
| $R_3$ |   2 |   $()$    | claw    | $(1,0,2,3)$            | $2$              |
| $R_3$ |   3 |   $(3)$   | $R_4$   | $(0,3,1,2)$            | $3,6$            |
| $R_3$ |   5 | $(0,1,2)$ | $R_4$   | $(0,2,1,3)$            | $5$              |
| $R_3$ |   7 |  $(1,2)$  | $R_4$   | $(0,2,1,3)$            | $7$              |
| $R_4$ |   1 |  $(0,1)$  | claw    | $(2,0,3,4)$            | $1,8$            |
| $R_4$ |   2 |   $()$    | claw    | $(1,0,2,4)$            | $2,4$            |
| $R_4$ |   3 |   $(1)$   | claw    | $(2,0,3,4)$            | $3,12$           |
| $R_4$ |   5 |   $()$    | claw    | $(2,1,3,4)$            | $5,10$           |
| $R_4$ |   6 |  $(1,4)$  | claw    | $(2,0,1,3)$            | $6$              |
| $R_4$ |   7 |   $(0)$   | claw    | $(2,1,3,4)$            | $7,14$           |
| $R_4$ |   9 |   $()$    | $R_5$   | $(0,1,2,3,4)$          | $9$              |
| $R_4$ |  11 |   $(0)$   | $R_5$   | $(0,1,2,3,4)$          | $11,13$          |
| $R_4$ |  15 |  $(1,0)$  | $R_5$   | $(0,1,4,3,2)$          | $15$             |
| $R_5$ |   1 |   $()$    | claw    | $(0,1,4,5)$            | $1,2,4,8,16$     |
| $R_5$ |   3 |   $(0)$   | claw    | $(4,1,3,5)$            | $3,6,12,17,24$   |
| $R_5$ |   5 |   $()$    | claw    | $(0,1,4,5)$            | $5,9,10,18,20$   |
| $R_5$ |   7 |   $(0)$   | claw    | $(2,1,3,5)$            | $7,14,19,25,28$  |
| $R_5$ |  11 |   $()$    | claw    | $(3,2,4,5)$            | $11,13,21,22,26$ |
| $R_5$ |  15 |   $(1)$   | claw    | $(3,2,4,5)$            | $15,23,27,29,30$ |
| $R_5$ |  31 |   $()$    | $R_6$   | $(0,1,2,3,4,5)$        | $31$             |

The machine-readable full certificate lists every attachment individually. It uses the field `n` for the *extended* size $k+1$, rather than for the base size $k$. The verifier checks coverage, distinctness, operation order and permutation direction explicitly.

## References

<a id="ref-FKMP"></a>

**\[1\]**

J. Fuentes, C. Keeler, W. Munizzi and J. Pollack, *Monogamy of Mutual Information in Graph States*, arXiv:2511.19585v1 \[quant-ph\], 24 November 2025. [arxiv.org/abs/2511.19585v1](https://arxiv.org/abs/2511.19585v1).

<a id="ref-Hein2004"></a>

**\[2\]**

M. Hein, J. Eisert and H.-J. Briegel, *Multiparty entanglement in graph states*, Physical Review A **69** (2004), 062311. [arXiv:quant-ph/0307130](https://arxiv.org/abs/quant-ph/0307130).

<a id="ref-Hein2006"></a>

**\[3\]**

M. Hein, W. Dür, J. Eisert, R. Raussendorf, M. Van den Nest and H.-J. Briegel, *Entanglement in Graph States and its Applications*, [arXiv:quant-ph/0602096](https://arxiv.org/abs/quant-ph/0602096) (2006).

<a id="ref-Bao"></a>

**\[4\]**

N. Bao, S. Nezami, H. Ooguri, B. Stoica, J. Sully and M. Walter, *The Holographic Entropy Cone*, Journal of High Energy Physics **09** (2015), 130. [doi:10.1007/JHEP09(2015)130](https://doi.org/10.1007/JHEP09(2015)130).

<a id="ref-KimOum"></a>

**\[5\]**

D. Kim and S. Oum, *Vertex-minors of graphs: A survey*, Discrete Applied Mathematics **351** (2024), 54–73. [doi:10.1016/j.dam.2024.03.011](https://doi.org/10.1016/j.dam.2024.03.011).

<a id="ref-KwonOum"></a>

**\[6\]**

O. Kwon and S. Oum, *Scattered classes of graphs*, [arXiv:1801.06004](https://arxiv.org/abs/1801.06004) (2018).

<a id="ref-Ascoli"></a>

**\[7\]**

R. Ascoli, B. Frederickson, S. Frederickson, C. McFarland and L. Post, *Almost all graphs are vertex-minor universal*, [arXiv:2602.09049v2](https://arxiv.org/abs/2602.09049v2), 20 February 2026.

<a id="ref-DabrowskiEtAl"></a>

**\[8\]**

K. K. Dabrowski, F. Dross, J. Jeong, M. M. Kanté, O.-j. Kwon, S.-i. Oum and D. Paulusma, *Computing pivot-minors*, Algorithmica **88** (2026), article 47. [doi:10.1007/s00453-026-01393-5](https://doi.org/10.1007/s00453-026-01393-5). Preprint: [arXiv:2311.04656v1](https://arxiv.org/abs/2311.04656v1).
