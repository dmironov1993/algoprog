#https://algoprog.ru/material/p2

def bin_search(a, length, target):
  left = 0
  right = length - 1
  while right >= left:
    middle = left + (right - left) // 2
    if array[middle] == target:
      return middle
    elif array[middle] > target:
      right = middle - 1
    else:
      left = middle + 1
  return (left, right)

if __name__ == "__main__":
  n, k = map(int, input().split())
  array = [*map(int, input().split())]
  elements = [*map(int, input().split())]
  for t in elements:
    ans = bin_search(array, n, t)
    if type(ans) == int:
      print(array[ans])
    else:
      left, right = ans
      if left > 0:
        left -= 1
      if right < n - 1:
        right += 1
      if abs(t - array[left]) > abs(t - array[right]):
        print(array[right])
      else:
        print(array[left])
