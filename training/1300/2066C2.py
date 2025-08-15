# title: 2066C2.py
# author: firekern
# date: 2025-08-15 22:55:53
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
    

    n, m = II()
    a = LI()
    b = LI()
    b.sort()
    c = [int(1e20)] * n

    c[0] = min(a[0],b[0] - a[0])
    for i in range(1, n):
        to_find = c[i - 1] + a[i]
        idx = bisect.bisect_left(b, to_find)

        if idx < m:
            c[i] = min(b[idx] - a[i],c[i])

        if a[i] >= c[i - 1] and a[i] >= c[i - 1]:
            c[i] = min(c[i], a[i])

        if c[i] == int(1e20):
            PRI("NO")
            return
    
    PRI("YES")

    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
