def find_the_ceiling_and_floor_of_a_number(a: list, k: int, start: int=None, end: int=None) -> dict:
  if start is None:
    start = 0
    end = len(a)

  mid = int((start + end) / 2)
  
  if a[mid] == k:
    return {"ceiling": a[mid], "floor": a[mid]}
  elif end - start == 1:
    if a[start] < k:
      return {"ceiling": -1, "floor": a[start]}
    else:
      return {"ceiling": a[start], "floor": -1}
  elif a[mid] < k and end - start > mid + 1:
    if a[mid + 1] > k:
      return {"ceiling": a[mid + 1], "floor": a[mid]}
  elif a[mid - 1] < k and a[mid] > k:
    return {"ceiling": a[mid], "floor": a[mid - 1]}
  
  if a[mid] > k:
    end = mid
  else:
    start = mid
  return find_the_ceiling_and_floor_of_a_number(a, k, start, end)


def print_ceiling_and_floor_of_each_number_in_an_array(a: list) -> None:
  length = 11
  for i in range(length):
    response = find_the_ceiling_and_floor_of_a_number(a, i)
    print(f"k = {i} --> teto = {response['ceiling']}, piso = {response['floor']}")


a = list(map(int, input().split()))
print_ceiling_and_floor_of_each_number_in_an_array(a)
