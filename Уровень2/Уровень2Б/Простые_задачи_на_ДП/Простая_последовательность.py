#https://algoprog.ru/material/p843

def seq(n):
  if n == 0:
    return 1
  if n == 1:
    return 1
  a = [0] * (2*n + 2)
  a[0] = 1
  a[1] = 1
  i = 2
  #while i < 2*n + 2:
  while i < n + 1:
    if i % 2 == 0:
      a[i] = a[i//2] + a[i//2-1]
    else:
      a[i] = a[i//2] - a[i//2-1]
    i += 1
  return a[n]

if __name__ == "__main__":
  n = int(input())
  print(seq(n))
