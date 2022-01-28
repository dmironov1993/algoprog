#https://algoprog.ru/material/p2771

n, m = map(int, input().split())
array = [*map(int, input().split())]

prefix = [0] * (n + 1)
for i in range(1, n+1):
    prefix[i] = prefix[i-1] + array[i-1]

for i in range(m):
    i, j = map(int, input().split())
    print(prefix[j] - prefix[i-1])
