Prover.py generates a list of equations that cannot be the first number to disprove the collatz conjecture
  It will also create a graph to help visualize how it got there (left is if k is even and right is if k is odd)

efficientCollatzGen.py will generate some c code where it will unroll the loop and will skip over the numbers that are proven to not be able to do the first
  (this method assumes that all values before the start value is true) - also does not yet support large numbers that cannot fit in an unsigned 128 bit integer.
 
 

Installation guidlines:
  download graphviz
