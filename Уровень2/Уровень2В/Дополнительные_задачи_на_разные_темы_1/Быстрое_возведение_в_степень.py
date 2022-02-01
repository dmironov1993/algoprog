#https://algoprog.ru/material/p3806

def pow(a, n):
  if n == 0:
    return 1
  if n % 2 == 0:
    c = pow(a, n // 2)
    return c * c
  else:
    return a * pow(a, n - 1)

if __name__ == "__main__":
  num = float(input())
  k = int(input())
  print(pow(num, k))
