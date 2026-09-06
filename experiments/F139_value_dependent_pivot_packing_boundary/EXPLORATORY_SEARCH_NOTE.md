# F139 exploratory-search note

An unregistered finite search first selected `N=667`. A hostile manual check
then found that its packed base word already factors the input:

```text
q = 133
iota_N(q) = 331
gcd(q + iota_N(q), 667) = 29
```

That certificate is invalid for the intended no-factor branch and is
preserved separately. A second unregistered search selected the fixed
`N=989` certificate. The searches only located readable witnesses. They
were not preregistered, their outputs are not artifacts, and they support no
density, probability, or all-input claim.

Only the revised fixed-certificate replay specified in
`PREREGISTRATION.md` is used as computation evidence.
