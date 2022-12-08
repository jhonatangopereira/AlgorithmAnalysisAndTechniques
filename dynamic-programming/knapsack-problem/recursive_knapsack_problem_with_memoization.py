# Recursive Knapsack solution with memoization

from random import randint
from time import time


def knapsack_problem_with_memoization(S:dict, i:int, W:int) -> int:
  if i == 0 or W == 0:
    return 0
  if mem[i][W] != -1:
    return mem[i][W]
  if S[i - 1]["weight"] > W:
    mem[i][W] = knapsack_problem_with_memoization(S, i - 1, W)
    return mem[i][W]
  mem[i][W] = max(
    knapsack_problem_with_memoization(S, i - 1, W),
    knapsack_problem_with_memoization(S, i - 1, W - S[i - 1]["weight"]) + S[i - 1]["value"]
  )
  return mem[i][W]

mem = [[-1 for i in range(1001)] for j in range(1001)]

S = dict()
for i in range(1000):
  S[i] = {"weight": randint(1, 6), "value": randint(10, 15)}

W = 80
start = time()
print(f"Result: {knapsack_problem_with_memoization(S, len(S), W)}")
end = time()
print(f"Time: {end - start}")
