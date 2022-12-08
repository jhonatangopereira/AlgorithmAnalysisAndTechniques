# Recursive Longest Common Subsequence solution

from random import choice
from time import time


def lcs(X, Y, m, n):
  if m == 0 or n == 0:
    return 0
  if X[m - 1] == Y[n - 1]:
    return 1 + lcs(X, Y, m - 1, n - 1)
  return max(
    lcs(X, Y, m, n - 1),
    lcs(X, Y, m - 1, n)
  )


start = time()

size = 12
X = "".join((choice('KGBNRYUO') for i in range(size)))
Y = "".join((choice('RWSDXQPL') for i in range(size)))
print(f"Result: {lcs(X, Y, size, size)}")

end = time()
print(f"Time: {end - start}")
