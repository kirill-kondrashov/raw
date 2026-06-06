# Loop spaces preserve locality

Fix a connected pointed space $M$.

## Quotations from Neisendorfer

Neisendorfer specifies the category and mapping-space notation as follows:

> We will work in the category of connected pointed spaces and pointed maps. But it still makes sense to consider $\operatorname{map}(A, B) =$ the space of all maps from $A$ to $B$. And $\operatorname{map}_*(A, B) =$ the subspace of all pointed maps from $A$ to $B$.

Neisendorfer does not define the phrase "pointed space" in the quoted sentence. Here it means a topological space with a chosen basepoint. Likewise, a pointed map means a continuous map sending the chosen basepoint of the source to the chosen basepoint of the target.

The exact definition of local space used below is:

> Definition 2.1.1: If $M$ is a fixed connected pointed space, then a connected pointed space $X$ is called $M$- null or local with respect to $M \to *$ if either of the following equivalent conditions hold:
>
> 1) the map which evaluates a function at the basepoint, $\operatorname{map}(M, X) \to X$, is a weak equivalence.
>
> 2) the space of pointed maps $\operatorname{map}_*(M, X)$ is weakly contractible.

Neisendorfer then states the equivalent worded form:

> The equivalence of the above two conditions is a consequence of the fibration sequence $\operatorname{map}_*(M, X) \to \operatorname{map}(M, X) \to X$.
>
> in other words, all pointed maps $\Sigma^n M \to X$ must be homotopic to the constant. In this sense, $M$ looks like a point with respect to $X$.

The exercise to be solved is:

> 1. a) Show that the loop space $\Omega(X)$ is local if $X$ is.

The suspension/evaluation adjoint pair used below is quoted from Neisendorfer:

> Define the suspension map $\Sigma = \Sigma_X : X \to \Omega\Sigma X$ by $\Sigma(x)(t) = \langle x,t\rangle$ for all $x \in X$ and $0 \leq t \leq 1$. This is just the adjoint of the identity map $1_{\Sigma X} : \Sigma X \to \Sigma X$. The other adjoint is the evaluation map $e = e_X : \Sigma\Omega X \to X$ with $e(\langle t,\omega\rangle) = \omega(t)$.

The symbols $\Sigma$, $\Omega$, $\operatorname{map}$, and $\operatorname{map}_*$ are therefore Neisendorfer's notation in the quoted text.

The letters $f$ and $H$ below are not Neisendorfer's notation. They are only temporary proof notation.

## Solution

Assume that $X$ is local. By Definition 2.1.1 and the quoted "in other words" sentence immediately following it, every pointed map of the following form is homotopic to the constant map.

**Formula (1).**

$$
\Sigma^n M \to X
$$

**Source of Formula (1).** This is Neisendorfer's sentence "all pointed maps $\Sigma^n M \to X$ must be homotopic to the constant." The inequality $n \geq 0$ is not written in that quoted sentence, but it is the range meant here for the iterated suspension notation $\Sigma^n M$ appearing there.

To prove that $\Omega X$ is local, Definition 2.1.1 says it is enough to prove that the following mapping space is weakly contractible.

**Formula (2).**

$$
\operatorname{map}_*(M,\Omega X)
$$

**Source of Formula (2).** This is Definition 2.1.1, condition 2), with $X$ replaced by $\Omega X$.

By the same quoted "in other words" sentence, again with $X$ replaced by $\Omega X$, it is enough to prove that every pointed map of the following form is homotopic to the constant map.

**Formula (3).**

$$
f \colon \Sigma^n M \to \Omega X
$$

**Source of Formula (3).** This comes from Neisendorfer's sentence "all pointed maps $\Sigma^n M \to X$ must be homotopic to the constant," with the target $X$ replaced by $\Omega X$. The letter $f$ is proof-only notation and is not quoted from Neisendorfer.

Neisendorfer's quoted evaluation formula is:

**Formula (4).**

$$
e_X(\langle t,\omega\rangle)=\omega(t)
$$

**Source of Formula (4).** This is quoted from Neisendorfer's suspension/evaluation adjoint-pair sentence:

> The other adjoint is the evaluation map $e = e_X : \Sigma\Omega X \to X$ with $e(\langle t,\omega\rangle) = \omega(t)$.

Apply Formula (4) to the value $\omega=f(z)$, where $z$ is a point of $\Sigma^n M$. This gives a pointed map:

**Formula (5).**

$$
\Sigma(\Sigma^n M) \to X,
\qquad
\langle t,z\rangle \mapsto f(z)(t)
$$

**Source of Formula (5).** This is not quoted verbatim from Neisendorfer. It is obtained by applying Neisendorfer's Formula (4), namely $e_X(\langle t,\omega\rangle)=\omega(t)$, to $\omega=f(z)$. Formula (5) is the map corresponding to Formula (3) under Neisendorfer's quoted sentence that the evaluation map is "the other adjoint."

The source $\Sigma(\Sigma^n M)$ is the next iterated suspension:

**Formula (6).**

$$
\Sigma^{n+1}M
$$

**Source of Formula (6).** This is not quoted verbatim from Neisendorfer. The iterated-suspension notation is present in Neisendorfer's quoted phrase "$\Sigma^n M$"; Formula (6) is the standard reading of one more suspension.

Thus Formula (5) is a pointed map of the following form:

**Formula (7).**

$$
\Sigma^{n+1}M \to X
$$

**Source of Formula (7).** This is not a separate quotation from Neisendorfer. It is Formula (5) rewritten using Formula (6).

By Formula (1), the pointed map in Formula (7) is homotopic to the constant map. Let $H$ be such a pointed homotopy:

**Formula (8).**

$$
H \colon \Sigma^{n+1}M \times I \to X
$$

**Source of Formula (8).** This is proof-only notation for the homotopy whose existence follows from Formula (1). The letter $H$ is not Neisendorfer's notation.

For a point $z$ of $\Sigma^n M$, define a path in $X$ by:

**Formula (9).**

$$
t \mapsto H(\langle t,z\rangle,s)
$$

**Source of Formula (9).** This is not quoted verbatim from Neisendorfer. It uses the same evaluation pattern as Neisendorfer's Formula (4), now applied to the homotopy $H$. Here $s$ is the homotopy parameter.

Formula (9) gives a pointed map $\Sigma^n M \to \Omega X$ for each value of $s$.

At the initial value of $s$, it is the original map Formula (3), because Formula (5) was defined by $\langle t,z\rangle \mapsto f(z)(t)$.

At the final value of $s$, it is the constant map:

**Formula (10).**

$$
\Sigma^n M \to \Omega X
$$

**Source of Formula (10).** This is not quoted from Neisendorfer. It is the constant map produced at the final value of the proof-only homotopy in Formula (8).

Thus the original pointed map is homotopic to the constant map:

**Formula (11).**

$$
f \colon \Sigma^n M \to \Omega X
$$

**Source of Formula (11).** This repeats the proof-only arbitrary map introduced in Formula (3).

Therefore every pointed map $\Sigma^n M \to \Omega X$ is homotopic to the constant map. By Neisendorfer's quoted Definition 2.1.1 and its quoted "in other words" reformulation, $\operatorname{map}_*(M,\Omega X)$ is weakly contractible. Hence $\Omega X$ is local.
