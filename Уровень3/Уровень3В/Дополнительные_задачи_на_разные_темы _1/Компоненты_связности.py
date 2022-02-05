#https://algoprog.ru/material/p111540

#from sys import setrecursionlimit
#import threading
#setrecursionlimit(10 ** 9)
#threading.stack_size(2 ** 26) 
#thread = threading.Thread(target = main)
#thread.start()

from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

n, m = map(int, input().split())
graph = {}
for _ in range(m):
  i, j = map(int, input().split())
  i -= 1
  j -= 1
  if i not in graph:
    graph[i] = set()
  graph[i].add(j)
  if j not in graph:
    graph[j] = set()
  graph[j].add(i)

used = [False] * n
color = [-1] * n

def dfs(v, used, cnt):
  used[v] = True
  color[v] = cnt
  for u in graph[v]:
    if not used[u]:
      dfs(u, used, cnt)

cnt = 0
for v in graph:
  if not used[v]:
    dfs(v, used, cnt)
    cnt += 1
for i in range(n):
  if color[i] == -1:
    color[i] = cnt
    cnt += 1
print(cnt)
d = dict()
for i in range(n):
  if color[i] not in d:
    d[color[i]] = []
  d[color[i]].append(i + 1)
for values in d.values():
  print(len(values))
  print(*values)
