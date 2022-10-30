def stuff(l: list, n: int):
  if n <= 1:
    return l[0]
  if l[0] < l[1]:
    l.remove(l[1])
  else:
    l.remove(l[0])
  stuff(l, n-1)

print(stuff([1, 2, 3, 4, 5], 5))