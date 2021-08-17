An inner product is a generalization of the dot product. In a vector space, it is a way
to multiply vectors together, with the result of this multiplication being a scalar.

More precisely, for a real vector space, an inner product <·,·> satisfies the following
four properties. Let u, v, and w be vectors and alpha be a scalar, then:

1. <u+v,w>=<u,w>+<v,w>.

2. <alphav,w>=alpha<v,w>.

3. <v,w>=<w,v>.

4. <v,v>>=0 and equal if and only if v=0.

The fourth condition in the list above is known as the positive-definite condition.
Related thereto, note that some authors define an inner product to be a function <·,·>
satisfying only the first three of the above conditions with the added (weaker)
condition of being (weakly) non-degenerate (i.e., if <v,w>=0 for all w, then v=0). In
such literature, functions satisfying all four such conditions are typically referred to
as positive-definite inner products (Ratcliffe 2006), though inner products which fail
to be positive-definite are sometimes called indefinite to avoid confusion. This
difference, though subtle, introduces a number of noteworthy phenomena: For example,
inner products which fail to be positive-definite may give rise to "norms" which yield
an imaginary magnitude for certain vectors (such vectors are called spacelike) and which
induce "metrics" which fail to be actual metrics. The Lorentzian inner product is an
example of an indefinite inner product.

A vector space together with an inner product on it is called an inner product space.
This definition also applies to an abstract vector space over any field.

Examples of inner product spaces include:

1. The real numbers R, where the inner product is given by

<x,y>=xy.
(1)

2. The Euclidean space R^n, where the inner product is given by the dot product

<(x_1,x_2,...,x_n),(y_1,y_2,...,y_n)>
=x_1y_1+x_2y_2+...x_ny_n
(2)

3. The vector space of real functions whose domain is an closed interval [a,b] with
   inner product

<f,g>=int_a^bfgdx.
(3)
When given a complex vector space, the third property above is usually replaced by

<v,w>=<w,v>^_,
(4)
where z^_ refers to complex conjugation. With this property, the inner product is called
a Hermitian inner product and a complex vector space with a Hermitian inner product is
called a Hermitian inner product space.

Every inner product space is a metric space. The metric is given by

g(v,w)=<v-w,v-w>.
(5)
If this process results in a complete metric space, it is called a Hilbert space. What's
more, every inner product naturally induces a norm of the form

|x|=sqrt(<x,x>),
(6)
whereby it follows that every inner product space is also naturally a normed space. As
noted above, inner products which fail to be positive-definite yield "metrics" - and
hence, "norms" - which are actually something different due to the possibility of
failing their respective positivity conditions. For example, n-dimensional Lorentzian
Space (i.e., the inner product space consisting of R^n with the Lorentzian inner
product) comes equipped with a metric tensor of the form

(ds)^2=-dx_0^2+dx_1^2+...+dx_(n-1)^2
(7)
and a squared norm of the form

|v|^2=-v_0^2+v_1^2+...+v_(n-1)^2
(8)
for all vectors v=(v_0,v_1,...,v_(n-1)). In particular, one can have negative
infinitesimal distances and squared norms, as well as nonzero vectors whose vector norm
is always zero. As such, the metric (respectively, the norm) fails to actually be a
metric (respectively, a norm), though they usually are still called such when no
confusion may arise.
