#https://algoprog.ru/material/p160

from collections import deque

n = int(input())
array = [[0]*n for _ in range(n)]
for i in range(n):
  array[i] = [*map(int, input().split())]
s, e = map(int, input().split())
s -= 1
e -= 1
dist = [None] * n
a = deque()
a.append(s)
dist[s] = 0
prev = [None] * n
prev[s] = -1
while a:
  v = a.popleft()
  for u in range(n):
    if array[v][u] and dist[u] is None:
        dist[u] = dist[v] + 1
        a.append(u)
        prev[u] = v
if dist[e] is not None:
  if dist[e] == 0:
    print(dist[e])
  else:
    path = []
    path.append(e + 1)
    final = prev[e]
    while prev[final] != -1:
      path.append(final + 1)
      final = prev[final]
    path.append(s + 1)
    print(dist[e])
    print(*path[::-1])
else:
  print(-1)
