A = [1, 3, 2, 5, 6, 2]
for j in range(1, len(A)):
  key = A[j]
  i = j - 1
  while i >= 0 and A[i] > key:
    A[i + 1] = A[i]
    i = i - 1
  A[i + 1] = key
print(A)
