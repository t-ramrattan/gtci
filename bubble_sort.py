import sys
from util import string_to_int_list
'''
Bubble Sort

[5, 7, 1, 3]
[5, 1, 3, 7]
[1, 3, 5, 7]
[1, 3, 5, 7]
[1, 3, 5, 7]

'''
arr = [5, 7, 1, 3]

def bubble_sort(arr):
  n = len(arr)
  for i in range(0, n):
    for j in range(1, n - i):
      if arr[j] < arr[j - 1]:
        arr[j - 1], arr[j] = arr[j], arr[j - 1]


def bubble_sort_optimized(arr):
  n = len(arr)
  for i in range(0, n):
    swapped = False    
    for j in range(1, n - i):
      if arr[j] < arr[j - 1]:
        swapped = True
        arr[j - 1], arr[j] = arr[j], arr[j - 1]
    
    if not swapped:
      break

'''
Complexity Analysis:
Runtime: O(n^2)
Space: O(1)

For the optimized version the worst case runtime complexity remains the same. However, the best runtime will be O(n)
when the array is already sorted.
'''


def main():
  arr = string_to_int_list(sys.argv[1])
  print(f'unsorted: {arr}')
  bubble_sort_optimized(arr)
  print(f'bubble sorted: {arr}')

if __name__ == '__main__':
  main()