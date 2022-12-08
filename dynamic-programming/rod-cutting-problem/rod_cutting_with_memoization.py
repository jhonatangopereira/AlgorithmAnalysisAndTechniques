# Rod cutting solution with memoization

def rod_cutting_with_memoization(p:list, n:int) -> int:
  r = {}
  r[0] = 0
  for i in range(1, n + 1):
    r[i] = -inf
  return rod_cutting_with_memoization_solver(p, n, r)


def rod_cutting_with_memoization_solver(p:list, n:int, r:dict) -> int:
  if r[n] >= 0:
    return r[n]
  q = 0
  for i in range(1, n + 1):
    q = max(q, p[i] + rod_cutting_with_memoization_solver(p, n - i, r))
  r[n] = q
  return q


print(rod_cutting_with_memoization)
