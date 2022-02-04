#https://algoprog.ru/material/p52

from collections import deque

s = input().split()
n = len(s)
q = deque([])
q.append(int(s[0]))
q.append(int(s[1]))
operations = {'+','-','*'}
for i in range(2, n):
  if s[i] in operations:
    second = q.pop()
    first = q.pop()
    if s[i] == '+':
      q.append(first + second)
    elif s[i] == '-':
      q.append(first - second)
    elif s[i] == '*':
      q.append(first * second)
  else:
    q.append(int(s[i]))
print(q[0])
