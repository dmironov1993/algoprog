#https://algoprog.ru/material/p174


n = int(input())
cnt = 0
seen = set()
for i in range(n):
  array = [*map(int, input().split())]
  for j in range(n):
    if array[j] == 1 and (i, j) not in seen and (j, i) not in seen:
      seen.add((i, j))
      cnt += 1
print(cnt)
