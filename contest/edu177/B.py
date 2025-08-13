# title: B.py
# author: firekern
# date: 2025-08-12 21:11:25
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

    n, k, x = II()
    a = LI()

    pfx = [0] * (2 * n + 1)
    pfx[0] = a[0]
    for i in range(1, n):
        pfx[i] = pfx[i - 1] + a[i]
    
    steps = [0] * n
    for i in range(n):
        
        k = bisect.bisect_right(pfx, pfx[i - 1] + x)

        if k < n:
            steps[i] = k
        else:
            q = x // pfx[n - 1]
            r 



    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
