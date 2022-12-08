from random import randint
from time import time


def initialize_matrix(m:list, n:int, W:int):
  for i in range(W + 1):
    m.append(list())
    for j in range(n + 1):
      if i == 0 or j == 0:
        m[i].append(0)
      else:
        m[i].append('-')

def knapsack_problem(S:dict, n:int, W:int) -> int:
  mem = list()
  initialize_matrix(mem, n, W)
  for i in range(1, n + 1):
    for w in range(1, W + 1):
      if S[i]["weight"] > w:
        mem[w][i] = mem[w][i - 1]
      else:
        mem[w][i] = max(mem[w - S[i]["weight"]][i - 1] + S[i]["value"], mem[w][i - 1])
  
  return mem[W][n]


S = dict()
for i in range(1, 10000):
  S[i] = {"weight": randint(1, 6), "value": randint(10, 15)}

start = time()
W = 80
print(f"Result: {knapsack_problem(S, len(S), 80)}")
end = time()
print(f"Time: {end - start}")
