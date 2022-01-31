#https://algoprog.ru/material/p623

def f(n):
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return i
  return n

if __name__ == "__main__":
  n = int(input())
  res = []
  while n > 1:
    number = f(n)
    res.append(number)
    n //= number
  print(*res, sep='*')

