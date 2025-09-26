
def insertion_sort(arr):
  n = len(arr)
  for i in range(1, n):
      key = arr[i]
      j = i - 1
      while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        print(f'i = {i}, j = {j}, key = {key} : arr = {arr}')        
        j -= 1
      arr[j + 1] = key
      print(f'i = {i}, j = {j}, key = {key} : arr = {arr}')      

'''
[3, 2, 1]
i = 1, j = 1, key = 2
[3, 3, 1]
i = 1, j = 0, key = 2
[2, 3, 1]

i = 2, j = 2, key = 1
[2, 3, 3]
i = 2, j = 1, key = 1
[2, 2, 3]
i = 2, j = 0, key = 1
[1, 2, 3]
'''


def main():
  arr = []
  print(f'unsorted: {arr}')
  insertion_sort(arr)
  print(f'sorted: {arr}')

  arr = [1]
  print(f'unsorted: {arr}')
  insertion_sort(arr)
  print(f'sorted: {arr}')

  arr = [3, 2, 1]
  print(f'unsorted: {arr}')
  insertion_sort(arr)
  print(f'sorted: {arr}')

  arr = [3, 2, 1, 7, 4, -1, - 12, 12, 10, 9, 100, -100]
  print(f'unsorted: {arr}')
  insertion_sort(arr)
  print(f'sorted: {arr}')  

if __name__ == '__main__':
  main()