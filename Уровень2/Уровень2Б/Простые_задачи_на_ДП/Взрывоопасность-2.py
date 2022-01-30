#https://algoprog.ru/material/p914

def seq(n):
  if n == 1:
    return 3
  if n == 2:
    return 8
  return 2*seq(n-1) + 2*seq(n-2)

if __name__ == "__main__":
  n = int(input())
  print(seq(n))
