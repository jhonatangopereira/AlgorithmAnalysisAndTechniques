# Recursive Knapsack solution

from random import randint
from time import time


def knapsack_problem(S:dict, i:int, W:int) -> int:
  if i == 0 or W == 0:
    return 0
  if S[i - 1]["weight"] > W:
    return knapsack_problem(S, i - 1, W)
  return max(
    knapsack_problem(S, i - 1, W),
    knapsack_problem(S, i - 1, W - S[i - 1]["weight"]) + S[i - 1]["value"]
  )


S = dict() # {0: {peso: 1, valor: 2}, 1: {peso: 2, valor: 5}}
for i in range(100):
  S[i] = {"weight": randint(1, 6), "value": randint(10, 15)}

W = 80
start = time()
print(f"Result: {knapsack_problem(S, len(S), W)}")
end = time()
print(f"Time: {end - start}")
