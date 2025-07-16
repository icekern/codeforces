# Created on: 16/07/2025 10:39:08
# Author: Porcelli
# GitHub: https://github.com/icekern/codeforces

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
    n = I()
    sett = [tuple(LI()) for _ in range(n)]
    sett = sett[::-1]

    pfx = [0] * (n + 1)

    for p in sett:
        pfx[p[0]] += 1

    for i in range(1, n + 1):
        pfx[i] += pfx[i - 1]
    
    sol = 0
    for i in range(n + 1):
        if (i,0) in sett and (i,1) in sett:
            sol += pfx[i - 1] if i > 0 else 0
            sol += pfx[n] - pfx[i]
        
        if 0 < i < n:
            if (i,0) in sett and (i-1,1) in sett and (i+1,1) in sett:
                sol += 1
            if (i,1) in sett and (i+1,0) in sett and (i-1,0) in sett:
                sol += 1

    PRI(sol)
    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()