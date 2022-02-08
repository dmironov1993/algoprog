#https://algoprog.ru/material/p111759

count = [0] * 26
s = input()
for el in s:
  count[ord('z') - ord(el)] += 1
ans = ''
count = count[::-1]
for j in range(25,-1,-1):
  if count[j] > 0:
    ans += chr(ord('a') + j) * count[j]
print(ans)
