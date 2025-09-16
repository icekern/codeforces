# Created on: 2025-08-09 22:54

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

# https://github.com/icekern/codeforces

DEBUG = 1
MULTI = True

def solve():
    n,q = II()
    a = LI()

    pfx = [0] * n
    pfx1 = [0] * n

    if a[0] == 1:
        pfx1[0] = a[0]

    for i in range(1, n):
        if a[i] == 1:
            pfx1[i] = pfx1[i - 1] + a[i]
        else:
            pfx1[i] = pfx1[i - 1]
    
    for i in range(1, n):
        pfx[i] = pfx[i - 1] + a[i]

    for _ in range(q):
        l, r = II()
        l -= 1
        r -= 1

        if l == 0:
            result = pfx[r]
        else:
            result = pfx[r] - pfx[l - 1]

        if result - (r - l + 1) - (pfx1[r] - (pfx1[l - 1] if l > 0 else 0)) >= 0 and l != r:
            PRI("YES")
        else:
            PRI("NO")

    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()