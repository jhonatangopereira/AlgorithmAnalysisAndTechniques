# Iterative bottom-up approach Rod Cutting problem.

def bottom_up_rod_cutting(p:list, n:int) -> int:
  mem = list()
  for i in range(n + 1):
    mem.append([])
    for j in range(n + 1):
      if i == 0 or j == 0:
        mem[i].append(0)
      else:
        if i == 1:
          mem[i].append(j * p[i - 1])
        elif i > j:
          mem[i].append(mem[i - 1][j])
        else:
          mem[i].append(max(p[i - 1] + mem[i][j - i], mem[i - 1][j]))
  
  return mem[n][n]

prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
number = 4
print(bottom_up_rod_cutting(prices, number))
