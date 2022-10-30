def linear_search(array:list, v:int) -> int | None:
  for i in range(len(array)):
    if v == array[i]:
      return i
  return None

print(linear_search([2, 4, 5, 8, 10], 10))