# title: C.py
# author: firekern
# date: 2025-09-13 16:42:06
# github: https://github.com/icekern/codeforces

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

    n,m = II()
    r = [LI() for _ in range(n)]
    a = [row[0] for row in r]
    b = [row[1] for row in r]

    sol = 0
    last_pos = 0
    last_side = 0

    for i in range(n):
        if (a[i] - last_pos) % 2 == 0:
            sol += (a[i] - last_pos) - (1 if last_side != b[i] else 0)
        else:
            sol += (a[i] - last_pos) - (1 if last_side == b[i] else 0)

        last_side = b[i]
        last_pos = a[i]
    
    if last_pos != m:
        sol += m - last_pos
        
    PRI(sol)


def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
