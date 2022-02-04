#https://algoprog.ru/material/p161

from collections import deque

n = int(input())
array = [[100500] * n for _ in range(n)]
x1, y1 = map(int, input().split())
x1 -= 1
y1 -= 1
array[x1][y1] = 0
x2, y2 = map(int, input().split())
x2 -= 1
y2 -= 1
step = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]
q = deque([(x1,y1)])
prev = [[None] * n for _ in range(n)]
prev[x1][y1] = (-1,-1)
while q:
  x, y = q.popleft()
  if x == - 1 and y == -1:
    break
  for dx, dy in step:
    xnew, ynew = x + dx, y + dy
    if xnew >= 0 and xnew < n and ynew >= 0 and ynew < n and array[xnew][ynew] > array[x][y] + 1:
      array[xnew][ynew] = array[x][y] + 1
      prev[xnew][ynew] = (x, y)
      q.append((xnew, ynew))
print(array[x2][y2])

path = []
path.append((x2,y2))
k = 1
while prev[path[-1][0]][path[-1][1]] != (-1,-1):
  xnext, ynext = prev[path[-1][0]][path[-1][1]]
  path.append((xnext, ynext))
  k += 1
for j in range(k-1,-1,-1):
  print(path[j][0] + 1, path[j][1] + 1)
