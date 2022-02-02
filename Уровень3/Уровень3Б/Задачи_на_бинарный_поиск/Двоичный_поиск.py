#https://algoprog.ru/material/p4

def bin_search(a, length, target):
  left = 0
  right = length - 1
  while right >= left:
    middle = left + (right - left) // 2
    if a[middle] == target:
      return 'YES'
    elif a[middle] > target:
      right = middle - 1
    else:
      left = middle + 1
  return 'NO'

if __name__ == "__main__":
  n, k = map(int, input().split())
  array = [*map(int, input().split())]
  elements = [*map(int, input().split())]
  for t in elements:
    print(bin_search(array, n, t))
