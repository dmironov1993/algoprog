#https://algoprog.ru/material/p973

def is_prime(n):
  if n == 1:
    return False
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  return True


if __name__ == '__main__':
  k = int(input())
  cnt, j = 0, 2
  while True:
    if is_prime(j):
      cnt += 1
    if cnt == k:
      break
    j += 1
  print(j)
