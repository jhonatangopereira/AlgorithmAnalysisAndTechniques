
def is_this_a_valid_array(array: list) -> bool:
  return sum(array) % 2 == 0


def calculate_two_subarrays_with_the_same_sum(array: list, mem: list=list(), item_index:int=0):
  if item_index >= len(array): return 0

  first_subarray = array[:item_index]
  second_subarray = array[item_index:]
  if sum(first_subarray) > sum(second_subarray): return 0

  if sum(first_subarray) == sum(second_subarray):
    return (first_subarray, second_subarray)
  
  return calculate_two_subarrays_with_the_same_sum(array=array, mem=mem, item_index=item_index + 1)


def split_array_into_two_subarrays_with_same_sum(array: list, mem: list=list()) -> bool:
  if mem == list():
    mem = [[False] * (int((sum(array) / 2) + 1)) for _ in range(len(array) + 1)]
    for i in range(len(mem)):
      mem[i][0] = True
  
  for i in range(1, len(array) + 1):
    for j in range(1, int((sum(array) / 2) + 1)):
      mem[i][j] = mem[i - 1][j]
      if j >= array[i - 1]:
        mem[i][j] = mem[i][j] | mem[i - 1][j - array[i - 1]]
  
  return mem[-1][-1]


if __name__ == '__main__':
  arrays = [[3, 1, 1, 2, 2, 1], [10, 8, 3, 5, 4, 9], [3, 6, 1, 8], [2, 1, 2, 1, 0, 1, 0, 1], [0, 4, 0, 2]]
  for array in arrays:
    print(array, end=" ")
    if is_this_a_valid_array(array=array):
      array = sorted(array)
      result = split_array_into_two_subarrays_with_same_sum(array=array)
      if result:
        print("possui dois subconjuntos válidos!")
      else:
        print("não possui dois subconjuntos válidos!")
    else:
      print("não é um array válido!")
