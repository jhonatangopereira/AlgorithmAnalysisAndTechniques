def selection_sort(array):
  n = len(array)

  for i in range(n-1): 
    minimum = i

    for j in range(i+1, n):
      if array[j] < array[minimum]:
        minimum = j

    if minimum != i:
      temp = array[i]
      array[i] = array[minimum]
      array[minimum] = temp

  return list

selection_sort([9, 8, 7, 4, 8, 5])