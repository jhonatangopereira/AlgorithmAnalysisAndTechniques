# Recursive Longest Common Subsequence solution

from random import choice
from time import time


size = 499
mem = [[-1 for _ in range(size)] for __ in range(size)]

def lcs_with_memoization(X, Y, m, n):
  if m == 0 or n == 0:
    return 0
  if mem[m - 1][n - 1] != -1:
    return mem[m - 1][n - 1]
  if X[m - 1] == Y[n - 1]:
    mem[m - 1][n - 1] = 1 + lcs_with_memoization(X, Y, m - 1, n - 1)
    return mem[m - 1][n - 1]
  mem[m - 1][n - 1] = max(
    lcs_with_memoization(X, Y, m, n - 1),
    lcs_with_memoization(X, Y, m - 1, n)
  )
  return mem[m - 1][n - 1]

start = time()
X = "".join((choice('KGBNRYUO') for _ in range(size)))
Y = "".join((choice('RWSDXQPL') for _ in range(size)))
print(f"Result: {lcs_with_memoization(X, Y, size, size)}")

end = time()
print(f"Time: {end - start}")
