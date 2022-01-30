#https://algoprog.ru/material/p206

n, m = map(int, input().split())

dp = [[0]*m for _ in range(n)]
dp[0][0] = 1
for x in range(n):
  for y in range(m):
    dx, dy = 1, 0
    if x + dx >= 0 and x + dx < n and y + dy >= 0 and y + dy < m:
      dp[x+dx][y+dy] += dp[x][y]
    dx, dy = 0, 1
    if x + dx >= 0 and x + dx < n and y + dy >= 0 and y + dy < m:
      dp[x+dx][y+dy] += dp[x][y]
print(dp[-1][-1])
