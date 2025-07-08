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

DEBUG = 1
MULTI = True 

def solve():
    # matrix n x n 
    # 1 ... n
    # . .   .
    # .  .  .
    # .   . .
    # 1 ... n

    # perm it
    # 1 2 3 4
    # 2 1 3 4
    # 3 2 1 4
    # 4 3 2 1
    # 5 4 3 2

    #  
    # 1 2 3 
    # 1 2 3
    # 1 2 3 

    # 1 2 3
    # 2 1 3
    # 3 2 1

    n = I()

    PRI(n - 1 + n - 2)
    for i in range(2,n + 1):
        PRI(i, 1, i)

    for i in range(1, n - 1):
        PRI(i, i + 1, n)


    pass


def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
