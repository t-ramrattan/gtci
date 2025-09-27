'''
https://www.geeksforgeeks.org/dsa/merge-sort/
'''
def merge(arr, left, mid, right):
  n1 = mid - left + 1
  n2 = right - mid

  # Create temp arrays
  L = [0] * n1
  R = [0] * n2

  # Copy data to temp arrays L[] and R[]
  for i in range(n1):
    L[i] = arr[left + i]
  
  for j in range(n2):
    R[j] = arr[mid + 1 + j]

  i = 0
  j = 0
  k = left
  
  # Merge the temp arrays back
  # into arr[left..right]

  while i < n1 and j < n2:
    if L[i] <= R[j]:
      arr[k] = L[i]
      i += 1
    else:
      arr[k] = R[j]
      j += 1
    k += 1
  
  # copy the remaining elements of L[],
  # if there are any

  while i < n1:
    arr[k] = L[i]
    i += 1
    k += 1
  
  # copy the remaining elements of R[],
  # if there are any
  while j < n2:
    arr[k] = R[j]
    j += 1
    k += 1

def mergeSort(arr, left, right):
  if left < right:
    mid = (left + right) // 2
    mergeSort(arr, left, mid)
    mergeSort(arr, mid + 1, right)
    merge(arr, left, mid, right)



def main():
  arr = [38, 27, 43, 10]
  print(arr)
  mergeSort(arr, 0, len(arr) - 1)
  print(arr)

if __name__ == '__main__':
  main()