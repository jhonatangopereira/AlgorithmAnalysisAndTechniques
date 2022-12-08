def fib(n:int) -> int:
  if n == 1 or n == 2:
    return 1
  if mem.get(n) != None:
    return mem.get(n)
  mem[n - 1] = fib(n - 1)
  mem[n - 2] = fib(n - 2)

  return mem[n - 1] + mem[n - 2]

mem = dict()
number = 8

print(f"{number}th number of Fibonacci sequence is: {fib(number)}")
