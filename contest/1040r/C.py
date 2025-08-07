# title: C.py
# author: firekern
# date: 2025-08-01 16:22:54
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
    n = I()
    pairs = [LI() for i in range(n)]
    for i in range(n):
        pairs[i].append(i + 1)

    pairs.sort(key=lambda x: (x[0],  -x[1]))

    sol = []
    last_ele = 0

    for i in range(n):
        if last_ele < pairs[i][1]:
            last_ele = pairs[i][1]
            sol.append(pairs[i][2])

    PRI(len(sol))
    PRI(*sol)
    

    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
