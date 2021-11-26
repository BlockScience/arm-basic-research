# algorithm notes

## Overview

This document contains and overview of the first version of the ARM, which is capable of learning in response to transactions on it.

## Definitions

There exists an a set of items $\mathcal{S}$. For each item $i\in \mathcal{S}$, there is a vector $x\in \mathbb{R}^n$ such that $x= M(i)$ where $M$ is an attribute map.

Suppose there has been a set of observations of items $i\in \mathcal{S}$ with attributes $x_i=M(i)$, then given a set of $m$ items from $\mathcal{S}$ it is possible to apply a clustering method $C:\mathcal{S}^m\rightarrow\mathcal{C}$, (such as k-means, or a Voronoi partition) to assign each item $i\in \mathcal{S}$ to exactly one cluster $j\in\mathcal{C}$ with a centroid $\bar x_j\in \mathbb{R}^n$; futher more let's set $|\mathcal{C}|=k$ to be the number of clusters. The items in cluster $j$ are denoted $\mathcal{C}_j \subset \mathcal{S}$, satisfying $S = 	\displaystyle{\bigsqcup_{j \in \mathcal{C}} C_j}$.

Now let's suppose we possess such a collection of $m$ items, sorted into into our $k$ clusters. Denote the quantity of items in cluster $j$ to be $q_j =\sum_{i =1}^m \mathbb{1}[i\in C_j]$, satisfying $\sum_{j=1}^k q_j=m$. Imposing a requirement on the method clustering method $C$, we will assume $q_j\ge 1 \forall j$.

Define the positive definite matrix $Q=Diag(q) \in \mathbb{S}_{++}^k \subset \mathbb{R}^{k \times k}$, which is the diagonal of the quantities of items each of the clusers: $Q_{jj}=q_j$ and $Q_{ij}=0$ for all $i\neq j$.

Construct the attribute matrix $X \in \mathbb{R}^{n \times k}$ by collecting the $n$-dimensional column vectors of cluster centroids $X=\left[\begin{array}{c} \cdots|&\bar x_j&|\cdots  \end{array}\right]$.

Combining the attribute matrix $X$ with the quantities of items $Q$ into a quadratic form yields the positive semidefinite matrix

$Z = XQX^T \in \mathbb{S}_+^n\subset \mathbb{R}^{n \times n}$, which has rank $l=\min(n,k)$. The Matrix $Z$ has a singular value decomposition $Z = V\Lambda V^T$ where $\Lambda = Diag(\lambda) \in \mathbb{S}_{++}^l \subset\mathbb{R}^{l \times l}$, the diagaonal matrix of eigenvalues, and $V=\left[\begin{array}{c}\cdots|& v_j&|\cdots\end{array}\right]\in\mathbb{R}^{n \times l}$.

It is still possible that $l$ is quite large. In order to allow for further dimensionality reduction, we may select the $p\le l$ largest eigenvalues to for $\hat \Lambda$ and associated eigenvectors $\hat V$ to approximate $Z$ with $\hat Z = \hat V \hat \Lambda\hat V^T$.

Let's suppose our market contains a quantity of a reserve currency $r$, in addition to quantities of items $q_j>0$ of items in clusters $\mathcal{C}_j$ with attribute vectors $\bar x_j$. Let the energy function for this market be given by
$$\Psi(r,q;X) = \prod_{j=1}^k \frac{\lambda_j(XQX^T)}{r} $$

keep in mind that both $X$ and $q$ are determined by applying a clustering algorithm to collection of $m$ items drawn from $\mathcal{S}$. Let us denote that collection $\mathcal{I}$ and refer to it as the inventory, where $m=|\mathcal{I}|$.

In the event that our market makes accepts an item into its inventory, the price it pays must increase its energy
$$\Psi(r-\Delta r, q+\Delta q; X) > \Psi(r, q; X)$$

following through with the manipulations
$$\Delta r < r\left(\sqrt[k]{\prod_{j=1}^k \frac{\lambda_j(X(Q+\Delta Q)X^T)}{\lambda_j(XQX^T)}} -1\right)$$

where $\Delta Q = Diag(\Delta q)$.

After completing a trade $(\Delta q, \Delta r)$, the market has an updated $\mathcal{I}$, so it is necessary to recompute the clusters $C_j$ and associated attribute vectors $X$.

In the event that our market releases an item from its inventory the energy function still must be increased
$$\Psi(r+\Delta r, q-\Delta q; X) > \Psi(r, q; X)$$

following through with the manipulations
$$\Delta r > r\left(1-\sqrt[k]{\prod_{j=1}^k \frac{\lambda_j(X(Q-\Delta Q)X^T)}{\lambda_j(XQX^T)}}\right)$$
where $\Delta Q = Diag(\Delta q)$.

After completing a trade $(\Delta q, \Delta r)$, the market has an updated $\mathcal{I}$, so it is necessary to recompute the clusters $C_j$ and associated attribute vectors $X$.

---

Observation: its dangerous to lose track of items that are not in the inventory, as they may be quite valuable. Rather than computing the clustering over the quantities of the items in the inventory, it might prudent to unstead maintain a record of all items $i \in \mathcal{S}$ ever observed as well as a summer statistic over the realized prices paid for that item. The candidate summary statistic exponentially smoothed average of realized prices. This way high priced items can retain their own clusters, even when they are rare, but we still need to contend with edge case handling if items of interest have 0 inventory.

Points for future consideration:
- choice of clustering algorithm
- choice of fee function
- overall sensitivity to high dimensional problem space
- convergence of eigenvalues and/or prices
- convergence of cluster and/or eigenvectors
- convergence rates

## Pseudo code

Given $\mathcal{I}$ and $r$
1. Apply Clustering method, return $X$ and $q$
2. if User sale event: $\Delta q$ in, payout $\Delta r$ such that $\Psi^+ > \Psi$
3. if User purchase event: $\Delta q$ out, pay in $\Delta r$ such that $\Psi^+ > \Psi$
4. Update $\mathcal{I}$ and $r$

The simplest method for computing an energy increasing $\Delta r$ would be first solve for $\Delta r$ such that $\Psi^+ = \Psi$ and then to apply a fee $\Delta r \leftarrow \Delta r(1-\phi)$ for outbound payments and $\Delta r \leftarrow \Delta r(1+\phi)$ for inbound payments.  