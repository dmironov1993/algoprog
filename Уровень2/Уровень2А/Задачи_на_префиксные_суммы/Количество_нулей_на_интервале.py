#https://algoprog.ru/material/p3313

if __name__ == "__main__":
    n = int(input())
    array = [*map(int, input().split())]
    
    cnt = [0 for _ in range(n)]
    cnt[0] = 1 if array[0] == 0 else 0
    for i in range(1, n):
        if array[i] == 0:
            cnt[i] = cnt[i-1] + 1
        else:
            cnt[i] = cnt[i-1]
                
    k = int(input())
    for i in range(k):
        left, right = map(int, input().split())
        left -= 1
        right -= 1
        if left > 0:
            print(cnt[right] - cnt[left-1])
        else:
            print(cnt[right])
