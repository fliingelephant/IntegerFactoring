# Primary-source checks

The candidate was stated before these checks. No knowledge-base metadata,
reference keys, or shared source files were modified.

- Andrew Sutherland, *18.783 Lecture7: Hasse's theorem and point counting*,
  MIT,2021. The notes provide the elliptic point-count bound used in the
  initial necessary test. The pole corrections in RESULT.md are derived
  separately by counting Artin-Schreier fibers; they are not assumed zero.
  [Official course PDF](https://ocw.mit.edu/courses/18-783-elliptic-curves-spring-2021/5e4e3bd15c9a81db2ac186628da095bf_MIT18_783S21_notes7.pdf).

- Shawn Farnell and Rachel Pries, *Families of Artin-Schreier curves with
  Cartier-Manin matrix of constant rank*, March13,2013, Sections2.1-2.2.
  For characteristic2 and reduced odd pole orders d_i, the genus is
  [sum_i(d_i+1)-2]/2. This supports the genus labels for the explicitly
  fitted rational functions; it does not identify the ring phase with one.
  [Author PDF](https://www.math.colostate.edu/~pries/Preprints/13ASfarnellpries313archive.pdf).

- Noam Elkies, Everett Howe, Andrew Kresch, Bjorn Poonen, Joseph Wetherell,
  and Michael Zieve, *Curves of every genus with many points, II*, Duke
  Mathematical Journal 122 (2004). The introduction states the general
  genus-g Weil bound, and the proof of Lemma2.1 uses both signs of it.
  This is the bound used in the higher-genus necessary envelope.
  [Author PDF](https://math.mit.edu/~poonen/papers/phewkz.pdf).

- Marko Moisio, *Kloosterman sums, elliptic curves, and irreducible
  polynomials with prescribed trace and norm*,2007, was checked as primary
  context for the field-character/curve connection. No theorem from it is
  used to turn a top ring digit into an additive field character.
  [Author paper](https://arxiv.org/html/0706.2112).

The full curve Hasse-Weil envelope is used only as a necessary condition,
with genus and finite-pole corrections stated explicitly. F310/C270 is
the closest repository record: its large fixed-order matrix rank motivated
testing a nonlinear trace, but was not used as evidence against fast scalar
summation.
