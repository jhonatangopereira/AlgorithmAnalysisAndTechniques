def find_the_first_occurrence_of_an_element(a: list, i: int, start: int=None, end:int=None) -> int:
  if start is None:
    start, end = 0, len(a)
  
  mid = int((start + end) / 2)

  if a[mid] == i:
    if mid == 0:
      return 0
    elif a[mid - 1] < i:
      return mid

  if a[mid] >= i:
    end = mid
  else:
    start = mid
  return find_the_first_occurrence_of_an_element(a, i, start, end)


def find_the_last_occurrence_of_an_element(a: list, i: int, start: int=None, end: int=None) -> int:
  if start is None:
    start, end = 0, len(a)
  
  mid = int((start + end) / 2)

  if a[mid] == i:
    if mid == len(a) - 1:
      return len(a)
    elif a[mid + 1] > i:
      return mid + 1
  
  if a[mid] <= i:
    start = mid
  else:
    end = mid
  return find_the_last_occurrence_of_an_element(a, i, start, end)


def find_the_frequency_of_an_element(a: list, i: int) -> int:
  first_position = find_the_first_occurrence_of_an_element(a, i)
  end_position = find_the_last_occurrence_of_an_element(a, i)
  
  return (end_position - first_position)


a = list(map(int, input().split()))
unique_elements = list(set(a))

for i in unique_elements:
  frequency = find_the_frequency_of_an_element(a, i)
  print(f"{i} ocorre {frequency} vez{'es' if frequency > 1 else ''}")
