#https://algoprog.ru/material/p912

def f(n):
  if n == 1:
    return 2
  if n == 2:
    return 4
  if n == 3:
    return 7
  return f(n-1) + f(n-2) + f(n-3)

if __name__ == "__main__":
  n = int(input())
  print(f(n))
