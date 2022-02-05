#https://algoprog.ru/material/p164

from sys import setrecursionlimit

n, s = map(int, input().split())
s -= 1
array = [[None]*n for _ in range(n)]
for i in range(n):
  array[i] = [*map(int, input().split())]

used = [False] * n
color = [-1] * n

def dfs(v, cnt):
  used[v] = True
  color[v] = cnt
  for u in range(n):
    if not used[u] and array[v][u] == 1:
      dfs(u, cnt)

cnt = 0
for v in range(n):
  if not used[v]:
    dfs(v, cnt)
    cnt += 1
for i in range(n):
  if color[i] == -1:
    color[i] = cnt
    cnt += 1
col = color[s]
ans = 0
for i in range(n):
  if color[i] == col:
    ans += 1
print(ans)
