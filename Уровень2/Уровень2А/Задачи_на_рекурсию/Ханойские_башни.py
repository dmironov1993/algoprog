#https://algoprog.ru/material/p3050

def tower(k, from_rod, aux_rod, to_rod):
    if k == 1:
        print(k, from_rod, to_rod)
        return
    tower(k - 1, from_rod, to_rod, aux_rod)
    print(k, from_rod, to_rod)
    tower(k - 1, aux_rod, from_rod, to_rod)

if __name__ == "__main__":
    n = int(input())
    tower(n,1,2,3)
