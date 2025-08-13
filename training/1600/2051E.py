# title: 2051E.py
# author: firekern
# date: 2025-08-11 14:45:56
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

    

    n,k = II()
    a = LI()
    b = LI()
    sol = 0
    l,r = 0, 10**9 + 1

    while l < r:
        mid = (l + r) // 2

        cnt = 0
        for i in range(n):
            if a[i] < mid:
                cnt += 1

        if cnt > k:
            r = mid
        else:
            sol = l
            l = mid + 1

        
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
