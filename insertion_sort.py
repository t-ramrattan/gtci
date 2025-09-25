import sys
from util import string_to_int_list
'''
https://www.geeksforgeeks.org/dsa/insertion-sort-algorithm/

Start at the second element
compare 2nd to first. If 2nd is less than first swap
Move to the next element. Compare the previous elements to the current
If current is less than any of the elements, swap it

Edge Cases:
- array is <= 1 : return


Examples:
[3,1,0]

[1,3,0]

[0,3,1]

[0,1,3]

'''


def insertion_sort(arr):
  n = len(arr)
  for i in range(1, n):
    key = arr[i] # Element to be inserted
    j = i - 1    # Index of the last element in the sorted subarray

    # Move elemens of arr[0..i-1], that are greater than key,
    # to one position ahead of their current position
    while j >= 0 and key < arr[j]:
      arr[j + 1] = arr[j] # shift element to the right
      j -= 1
    
    arr[j + 1] = key # insert the key in the correct position

def main():
  arr = string_to_int_list(sys.argv[1])
  print(f'unsorted: {arr}')
  insertion_sort(arr)
  print(f'sorted: {arr}')

if __name__ == '__main__':
  main()


'''
Complexity Analysis:
Time: O(n^2)
Space: O(1)
'''