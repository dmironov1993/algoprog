#https://algoprog.ru/material/p913

def seq(n):
  first = [0] * n
  first[0] = 1
  second = [0] * n
  second[0] = 1
  for i in range(1, n):
    first[i] = second[i-1]
    second[i] = first[i-1] + second[i-1]
  return first[n-1] + second[n-1]

if __name__ == "__main__":
  n = int(input())
  print(seq(n))
