#https://algoprog.ru/material/p1441

def gcd(a, b):
  return a if b == 0 else gcd(b, a % b)

n = int(input())
array = [*map(int, input().split())]
if n == 1:
  print(array[0])
else:
  d = gcd(array[0], array[1])
  for i in range(2, n):
    d = gcd(d, array[i])
  print(d)
