#https://algoprog.ru/material/p203

def sol(n):
  if n == 1:
    return 1
  if n == 2:
    return 2 
  dp = [0] * (n + 1)
  dp[0] = 1
  dp[1] = 1
  dp[2] = 2
  for i in range(3, n + 1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
  return dp[-1]

if __name__ == "__main__":
  n = int(input())
  print(sol(n))
