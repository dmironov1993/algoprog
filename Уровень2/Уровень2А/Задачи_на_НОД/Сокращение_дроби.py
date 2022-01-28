#https://algoprog.ru/material/p27

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a, b = map(int, input().split())
c, d = a, b
div = gcd(a, b)
while c != div and d != div and div != 1:
    c //= div
    d //= div
    div = gcd(c, d)
print(c // div, d // div)
