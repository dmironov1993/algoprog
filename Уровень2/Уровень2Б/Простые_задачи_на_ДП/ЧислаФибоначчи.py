#https://algoprog.ru/material/p201

def fib(n):
  if n == 1:
    return 1
  if n == 2:
    return 1
  prev = 1
  cur = 1
  i = 2
  while i < n:
    tmp = cur
    cur += prev
    prev = tmp
    i += 1
  return cur

if __name__ == "__main__":
  n = int(input())
  print(fib(n))
