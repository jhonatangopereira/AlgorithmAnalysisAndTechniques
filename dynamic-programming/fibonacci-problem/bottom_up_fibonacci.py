# Iterative bottom-up approach Fibonacci problem.

def fib(n:int) -> int:
  mem = dict()
  mem[1] = 1
  mem[2] = 1
  for i in range(3, n + 1):
    mem[i] = mem[i - 1] + mem[i - 2]
  
  return mem[n]


'''
With bottom-up approach, it's possible to calculate highest
numbers in Fibonacci sequence, using just a few seconds to
return.
'''
number = 10000
print(fib(number))
