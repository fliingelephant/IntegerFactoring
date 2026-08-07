# F89 reconstruction correction certificate

The original reconstruction statement has SHA-256

~~~text
aafa64e607c6cd108b08b43d3084a91ca388930792c569db083c4b9d9e58fabe
~~~

The corrected statement has SHA-256

~~~text
e504a24c285e0c98d64a37302e53e56b6656ec50361a507e003f37a1848d5779
~~~

A direct diff shows three presentation edits:

1. the title now labels the statement as corrected;
2. the opening sentence records the mechanical correction; and
3. the density display replaces the two form-feed-plus-rac defects with the
   intended fraction commands.

The third item is the only change to a mathematical expression. It produces

\[
\frac1A+\frac1B-\frac2{AB},
\]

which is exactly the formula reconstructed and proved in the existing
result. The existing PASS proof therefore applies unchanged to the corrected
statement.

The unchanged reconstruction result has SHA-256

~~~text
8d0948ae5348e5a67772f13f4b7a9249a25a85be6752ef229fd41bc51a4816f5
~~~
