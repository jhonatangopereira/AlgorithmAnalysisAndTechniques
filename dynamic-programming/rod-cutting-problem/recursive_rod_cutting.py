# Recursive Rod Cutting solution

def recursive_rod_cutting(prices:list, n:int) -> int:
  if n == 0:
    return 0
  q = 0
  for i in range(1, n + 1):
    q = max(q, prices[i] + algoritmo(prices, n - i))

  return q


prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
number = 4
print(algoritmo(prices, number))
