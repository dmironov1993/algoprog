#https://algoprog.ru/material/p447

import math

x1,y1 = map(int, input().split())
l1 = math.sqrt(x1*x1 + y1*y1)
x2,y2 = (1,0)
l2 = abs(x2)
if l1 == 0 or l2 == 0:
  print(0)
else:
  angle = math.acos((x1*x2 + y1*y2) / (l1 * l2))
  if y1 >= 0:
    print(angle)
  else:
    print(2 * math.pi - angle)
