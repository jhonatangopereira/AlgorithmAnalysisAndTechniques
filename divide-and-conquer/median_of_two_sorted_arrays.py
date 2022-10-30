def calculate_median(a: list, b: list, start_a: int=None, end_a: int=None, start_b: int=None, end_b: int=None) -> int:
  if start_a is None:
    start_a = start_b = 0
    end_a = end_b = len(a)
  
  mid_a = int((start_a + end_a) / 2)
  mid_b = int((start_b + end_b) / 2)

  if a[mid_a] == b[mid_b]:
    return a[mid_a]

  if end_a - start_a == 1:
    return int((a[start_a] + b[start_b]) / 2)
  elif end_a - start_a == 2:
    result = [max(a[start_a], b[start_b]), min(a[start_a + 1], b[start_a + 1])]
    return int(sum(result) / 2)
  elif a[mid_a] < b[mid_b]:
    return calculate_median(a, b, mid_a + 1, end_a, start_b, mid_b)
  else:
    return calculate_median(a, b, start_a, mid_a, mid_b + 1, end_b)

array_size = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(calculate_median(A, B))