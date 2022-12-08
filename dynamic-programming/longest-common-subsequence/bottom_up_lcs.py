# Recursive Longest Common Subsequence solution

from random import choice
from time import time


size = 1000

def lcs_with_memoization(X, Y, m, n):
  mem = [[-1 for i in range(size + 1)] for j in range(size + 1)]

  for i in range(m + 1):
    for j in range(n + 1):
      if i == 0 or j == 0:
        mem[i][j] = 0
      elif X[i - 1] == Y[i - 1]:
        mem[i][j] = 1 + mem[i - 1][j - 1]
      else:
        mem[i][j] = max(
          mem[i - 1][j],
          mem[i][j - 1]
        )
  return mem[-1][-1]

start = time()
X = "".join((choice('KGBNRYUO') for i in range(size)))
Y = "".join((choice('RWSDXQPL') for i in range(size)))
print(f"Result: {lcs_with_memoization(X, Y, size, size)}")

end = time()
print(f"Time: {end - start}")
