#https://algoprog.ru/material/p49

import sys

d = dict()

for i in range(6):
  s = input().split()
  n, name = int(s[0]), s[1]
  if n not in d:
    d[n] = []
  d[n].append(name.encode('cp866'))

for i in [9,10,11]:
  if i in d:
    for j, el in enumerate(d[i]):
      print(i, el.decode('cp866'))
