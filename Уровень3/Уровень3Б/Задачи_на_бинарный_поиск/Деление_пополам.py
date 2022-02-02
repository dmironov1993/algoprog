#https://algoprog.ru/material/p3570

EPS = 1e-7

def half_div(a, n):
  left = 0
  right = max(a, 1)
  while right - left > EPS:
    middle = left + (right - left) / 2
    if middle ** n > a:
      right = middle
    else:
      left = middle
  return middle

if __name__ == "__main__":
  a = float(input())
  n = int(input())
  print(half_div(a, n))
