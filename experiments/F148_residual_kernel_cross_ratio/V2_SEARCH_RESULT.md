# F148 V2 finite-search result — rejected certificate

The frozen V2 search returned

`N=115, d=6, a=11, b=34, u=4, v=19`.

The four exact values are distinct and the combined arithmetic is correct.
However, both canonical endpoints are self-inverse. In particular,
`c1=w1=24` is already a non-global square root of one. Its one canonical
value is the exact square `24^2`, so the ordinary P66 decoder can factor the
input before the cross-cycle combination. V2 is rejected as a clean witness
for the new mechanism.
