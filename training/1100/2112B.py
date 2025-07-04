import sys
from collections import defaultdict, deque
import math
import heapq
import bisect

def input(): return sys.stdin.readline().rstrip('\n')
def I(): return int(input())
def II(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def SI(): return input().split()
def PRI(*args, **kwargs):
    if DEBUG == 1:
        green = "\033[92m"
        reset = "\033[0m"
        print(f"{green}{kwargs.get('sep', ' ').join(map(str, args))}{reset}", **kwargs)
    else:
        print(*args, **kwargs)

DEBUG = 0
MULTI = True 

def solve():

    n = I()
    a = LI()
    sol = int(1e9)
    for i in range(n):

        mas, minn = 0, int(1e9)

        for j in range(i + 1, n):
            mas = max(mas, a[j])
            minn = min(minn, a[j])
            if minn - 1 <= a[i] <= mas + 1:
                sol = min(sol, abs(i - j) - 1)
        
        mas, minn = 0, int(1e9)
        for j in range(i - 1, -1 , -1):
            mas = max(mas, a[j])
            minn = min(minn, a[j])     
            if minn - 1 <= a[i] <= mas + 1:
                sol = min(sol, abs(i - j) - 1)

    PRI(sol if sol != int(1e9) else -1)
    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
