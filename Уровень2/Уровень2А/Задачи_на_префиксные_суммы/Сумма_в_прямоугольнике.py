#https://algoprog.ru/material/p2772

n, m, k = map(int, input().split())
array = [[0] * m for _ in range(n)]
for i in range(n):
  array[i] = [*map(int, input().split())]
prefix = [[0] * m for _ in range(n)]
for i in range(n):
  for j in range(m):
    if i == 0 and j == 0:
      prefix[i][j] = array[i][j]
    elif i >= 1 and j == 0:
      prefix[i][j] = array[i][j] + prefix[i-1][-1]
    else:
      prefix[i][j] = array[i][j] + prefix[i][j-1]
for _ in range(k):
  x1, y1, x2, y2 = map(int, input().split())
  x1 -= 1
  y1 -= 1
  x2 -= 1
  y2 -= 1
  cnt = 0
  for i in range(x1, x2 + 1):
    if i == 0 and y1 == 0:
      cnt += prefix[i][y2]
    elif i >= 1 and y1 == 0:
      cnt += prefix[i][y2] - prefix[i-1][-1]
    else:
      cnt += prefix[i][y2] - prefix[i][y1-1]
  print(cnt)
