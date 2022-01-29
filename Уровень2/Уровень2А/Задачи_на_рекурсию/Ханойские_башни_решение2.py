#https://algoprog.ru/material/p3050

def tower(n, i, k):
    if n == 1:
        print(1, i, k)
    else:
        tmp = 6 - i - k
        tower(n - 1, i, tmp)
        print(n, i, k)
        tower(n - 1, tmp, k)
        
if __name__ == '__main__':
    n = int(input())
    tower(n, 1, 3)
