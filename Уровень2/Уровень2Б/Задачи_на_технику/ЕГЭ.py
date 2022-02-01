#https://algoprog.ru/material/p848

s = input()
n = len(s)
for i in range(1, n):
  if s[i-1].isdigit() and s[i].isdigit() and int(s[i-1:i+1]) > 5:
    print("NO")
    break
  if (s[i-1].isdigit() and int(s[i-1]) > 5) or (s[i].isdigit() and int(s[i]) > 5):
    print("NO")
    break
else:
  print("YES")
