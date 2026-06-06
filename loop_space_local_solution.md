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

The symbols $\Sigma$, $\Omega$, $\operatorname{map}$, and $\operatorname{map}_*$ are therefore Neisendorfer's notation in the quoted text. The letter $f$ below is not Neisendorfer's notation; it is only a temporary name for an arbitrary pointed map in the proof.

## Solution

Assume that $X$ is local. By Definition 2.1.1 and the quoted "in other words" sentence immediately following it, every pointed map

$$
\Sigma^n M \to X
\tag{1}
$$

is homotopic to the constant map, for every $n \geq 0$. Formula (1) comes from Neisendorfer's sentence "all pointed maps $\Sigma^n M \to X$ must be homotopic to the constant." The inequality $n \geq 0$ is not written in that quoted sentence, but it is the range meant here for the iterated suspension notation $\Sigma^n M$ appearing in that sentence.

To prove that $\Omega X$ is local, Definition 2.1.1 says it is enough to prove that

$$
\operatorname{map}_*(M,\Omega X)
\tag{2}
$$

is weakly contractible. Formula (2) comes from Definition 2.1.1, condition 2), with $X$ replaced by $\Omega X$. By the same quoted "in other words" sentence, again with $X$ replaced by $\Omega X$, it is enough to prove that every pointed map

$$
f \colon \Sigma^n M \to \Omega X
\tag{3}
$$

is homotopic to the constant map. Formula (3) comes from Neisendorfer's sentence "all pointed maps $\Sigma^n M \to X$ must be homotopic to the constant," with the target $X$ replaced by $\Omega X$ and with the temporary proof name $f$ added. The letter $f$ is not Neisendorfer's notation.

Neisendorfer's quoted evaluation formula, from the suspension/evaluation adjoint pair quoted above, is

$$
e_X(\langle t,\omega\rangle)=\omega(t).
\tag{4}
$$

Apply this formula to the value $\omega=f(z)$, where $z$ is a point of $\Sigma^n M$. This gives a pointed map

$$
\Sigma(\Sigma^n M) \to X,
\qquad
\langle t,z\rangle \mapsto f(z)(t).
\tag{5}
$$

Formula (5) is not quoted verbatim from Neisendorfer. It is obtained by applying Neisendorfer's formula (4), namely $e_X(\langle t,\omega\rangle)=\omega(t)$, to the value $\omega=f(z)$. The display (5) is exactly the map corresponding to (3) under Neisendorfer's quoted sentence that the evaluation map is "the other adjoint." No extra bracket notation is being introduced here.

The source $\Sigma(\Sigma^n M)$ is the next iterated suspension, written

$$
\Sigma^{n+1}M.
\tag{6}
$$

Formula (6) is not quoted verbatim from Neisendorfer. The iterated-suspension notation is present in Neisendorfer's quoted phrase "$\Sigma^n M$"; equation (6) is only the standard reading of one more suspension.

Thus (5) is a pointed map

$$
\Sigma^{n+1}M \to X.
\tag{7}
$$

Formula (7) is not a separate quotation from Neisendorfer; it is formula (5) rewritten using formula (6). By (1), the pointed map (7) is homotopic to the constant map. Let $H$ be such a pointed homotopy:

$$
H \colon \Sigma^{n+1}M \times I \to X.
\tag{8}
$$

Formula (8) is proof-only notation for the homotopy whose existence follows from formula (1). The letter $H$ is not Neisendorfer's notation.

For a point $z$ of $\Sigma^n M$, define a path in $X$ by

$$
t \mapsto H(\langle t,z\rangle,s).
\tag{9}
$$

Formula (9) is not quoted verbatim from Neisendorfer. It uses the same evaluation pattern as Neisendorfer's formula (4), now applied to the homotopy $H$. Here $s$ is the homotopy parameter. Formula (9) gives a pointed map $\Sigma^n M \to \Omega X$ for each value of $s$. At the initial value of $s$, it is the original map (3), because (5) was defined by $\langle t,z\rangle \mapsto f(z)(t)$. At the final value of $s$, it is the constant map

$$
\Sigma^n M \to \Omega X.
\tag{10}
$$

Formula (10) is not quoted from Neisendorfer. It is the constant map produced at the final value of the proof-only homotopy (8).

Thus the original pointed map

$$
f \colon \Sigma^n M \to \Omega X
\tag{11}
$$

is homotopic to the constant map. Formula (11) repeats the proof-only arbitrary map introduced in formula (3).

Therefore every pointed map $\Sigma^n M \to \Omega X$ is homotopic to the constant map. By Neisendorfer's quoted Definition 2.1.1 and its quoted "in other words" reformulation, $\operatorname{map}_*(M,\Omega X)$ is weakly contractible. Hence $\Omega X$ is local.
