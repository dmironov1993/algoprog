#https://algoprog.ru/material/p50

from collections import deque

s1 = deque([*map(int, input().split())])
s2 = deque([*map(int, input().split())])

cnt = 0
while s1 and s2 and cnt < 10**6:
  cnt += 1
  f = s1.popleft()
  s = s2.popleft()
  if (f == 0 and s == 9):
    s1.extend([f, s])
  elif (f == 9 and s == 0):
    s2.extend([f, s])
  elif (f > s):
    s1.extend([f, s])
  else:
    s2.extend([f, s])
if cnt == 10**6:
  print('botva')
elif s1 and not s2:
  print('first', cnt)
else:
  print('second', cnt)
