'''
Divide an conquer algorithm

functions 
- merge
- mergeSort


Examples:
[3,2,1]
left = 0 
right = 4
mid = right - left // 2


'''

def merge(arr, left, mid, right):
  # determine the size of the subarrays
  n1 = mid - left + 1 # 2 - 0  = 2
  n2 = right - mid # 4 - 2 = 2

  # create subarrays
  L = [0] * n1
  R = [0] * n2

  # copy values to subarrays
  for i in range(n1):
    L[i] = arr[left + i]

  for j in range(n2):
    R[j] = arr[mid + 1 + j]
  
  
  # merge
  i = 0
  j = 0
  k = left
  
  print(f'L = {L} n1 = {n1} i = {i}, R = {R} n2 = {n2} j = {j}, k = {k} arr= {arr}')
  
  while i < n1 and j < n2:
    if L[i] <= R[j]:
      arr[k] = L[i]
      i += 1
    else:
      arr[k] = R[j]
      j += 1     
    k += 1
    print(f'L = {L} n1 = {n1} i = {i}, R = {R} n2 = {n2} j = {j}, k = {k} arr= {arr}')
  
  while i < n1:
    arr[k] = L[i]
    i += 1
    k += 1
    print(f'L = {L} n1 = {n1} i = {i}, R = {R} n2 = {n2} j = {j}, k = {k} arr= {arr}')
  
  while j < n2:
    arr[k] = R[j]
    j += 1
    k += 1
    print(f'L = {L} n1 = {n1} i = {i}, R = {R} n2 = {n2} j = {j}, k = {k} arr= {arr}')     

def mergeSort(arr, left, right):
  if left >= right:
    return

  mid = (left + right) // 2
  mergeSort(arr, left , mid)
  mergeSort(arr, mid + 1, right)
  merge(arr, left, mid, right)


def main():
  arr = [3,2,1]
  print(arr)
  mergeSort(arr, 0, len(arr) - 1)
  print(arr)

  arr = [38, 27, 43, 10]
  print(arr)
  mergeSort(arr, 0, len(arr) - 1)
  print(arr)

if __name__ == '__main__':
  main()