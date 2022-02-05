#https://algoprog.ru/material/p51

from collections import deque

s = input()
n = len(s)
d = deque([])
for i in range(n):
  if s[i] == '(':
    d.append(')')
  elif s[i] == '[':
    d.append(']')
  elif s[i] == '{':
    d.append('}')
  elif d:
    el = d.pop()
    if el != s[i]:
      print('no')
      break
    else: 
      continue
  else:
    print('no')
    break
else:
  if not d:
    print('yes')
  else:
    print('no')
