def bubble_sort(array):
  n = len(array)

  for _ in range(n - 1):
    for j in range(n - 1):
      if array[j] > array[j + 1]: 
        tmp = array[j]
        array[j] = array[j + 1]
        array[j + 1] = tmp

  print(array)

print(bubble_sort([2, 5, 8, 3, 9, 4, 1]))