# F148 V1 finite-search result — rejected certificate

The frozen V1 search returned

`N=85, d=19, a=23, b=28, u=v=2`.

Its arithmetic cross-ratio certificate is valid, but it is not a clean
four-column P128 certificate. Both cycles have the same canonical endpoint
`c=38` and the same canonical exact value `1786`. Global exact-value
deduplication therefore removes one copy. Also, the V1 script divided the
positive root by `c1*c2` a second time when it reported the normalized root.
For the actual canonical/lifted relation list, whose supplied roots are all
one, the normalized root is the positive integer root itself modulo `N`.

The V1 output is rejected as evidence for the stated four-column form. Its
two lifted columns do in fact give a smaller valid dependency, but V2 will
require four distinct exact values and will correct the root evaluator.
