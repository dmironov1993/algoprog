#https://algoprog.ru/material/p154

def gcd(a, b):
    if not b:
        return a
    return gcd(b, a % b)

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
