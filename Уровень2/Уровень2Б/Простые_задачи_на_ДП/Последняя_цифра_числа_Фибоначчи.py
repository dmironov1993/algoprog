#https://algoprog.ru/material/p842

def fib(n):
  if n == 0:
    return 1
  if n == 1:
    return 1
  prev = 1
  cur = 1
  i = 1
  while i < n:
    tmp = cur
    cur += prev
    prev = tmp
    i += 1
  return str(cur)[-1]
  
if __name__ == "__main__":
  n = int(input())
  print(fib(n))
