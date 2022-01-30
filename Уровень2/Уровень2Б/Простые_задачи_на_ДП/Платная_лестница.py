#https://algoprog.ru/material/p915

n = int(input())
array = [*map(int, input().split())]

dp = [0] * (n + 1)
dp[1] = array[0]
for i in range(2, n + 1):
  dp[i] = min(dp[i-1], dp[i-2]) + array[i-1]
print(dp[-1])
