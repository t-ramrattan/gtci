'''
  1. Divide and Conquer: Like Merge Sort, Quick Sort is a divide-and-conquer algorithm.
  2. In-place (mostly): Unlike Merge Sort, which typically requires O(n) extra space for merging, Quick Sort can often be implemented in-place (or with
     O(log n) auxiliary space for the call stack), making it more memory-efficient.
  3. Performance Comparison: It's important to understand both Quick Sort and Merge Sort as they are two of the most efficient comparison-based sorting
     algorithms, each with its own strengths and weaknesses (e.g., worst-case performance, stability).
  4. Partitioning Strategy: Quick Sort's core idea revolves around a "partitioning" step, which is a fundamental technique used in many other algorithms
     (like finding the k-th smallest element).

  Learning Quick Sort will deepen your understanding of sorting algorithms and introduce you to new techniques.

- https://www.geeksforgeeks.org/dsa/quick-sort-algorithm/
- https://www.youtube.com/watch?v=Vtckgz38QHs


Pick a pivot.
All items to the left of the pivot must be less than it
All right to the right of the pivot must be greater than the pivot

have to start i is less than 1 of the beginning of the array

if value at j is less than pivot then we increment i then swap (i and j)

'''

def swap(arr, i , j):
  arr[i],arr[j] = arr[j],arr[i]

def partition(arr, low, high):
  pivot = arr[high]
  i = low - 1

  for j in range(low, high):
    if arr[j] < pivot:
      i += 1
      swap(arr, i, j)
  
  i += 1
  swap(arr, i, high)
  return i

def quick_sort(arr, low, high):
  if high <= low:
   return
  pi = partition(arr, low, high)
  quick_sort(arr, low, pi - 1)
  quick_sort(arr, pi + 1, high)
    

def main():
  arr = [3,1,2, -1, 5, 7, 12, 100, -10, 50]
  print(arr)
  quick_sort(arr, 0, len(arr) - 1)
  print(arr)

if __name__ == '__main__':
  main()