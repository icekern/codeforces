# title: 1419C.py
# author: firekern
# date: 2025-08-13 23:31:13
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
    n, x = II()
    a = LI()
    a.sort()

    if a.count(x) == n:
        PRI(0)
    else:
        diff = 0
        for i in range(n):
            diff += a[i] - x

        if diff == 0 or a.count(x) > 0:
            PRI(1)
        else:
            PRI(2)

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
