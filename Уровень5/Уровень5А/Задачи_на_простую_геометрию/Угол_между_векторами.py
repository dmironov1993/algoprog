#https://algoprog.ru/material/p448

import math

x1,y1,x2,y2 = map(int, input().split())
l1 = x1*x1 + y1*y1
l2 = x2*x2 + y2*y2
print(math.acos((x1*x2 + y1*y2) / (math.sqrt(l1) * math.sqrt(l2))))
