#https://algoprog.ru/material/p1838

def gcd(a, b):
  return a if not b else gcd(b, a % b)

if __name__ == "__main__":
  x1,y1,x2,y2 = map(int, input().split())
  dx = abs(x1 - x2)
  dy = abs(y1 - y2)
  print(dx + dy - gcd(dx, dy))
