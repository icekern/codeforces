# title: 2131F.py
# author: firekern
# date: 2025-08-13 22:13:15
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
    a = input()
    b = input()

    a = [int(x) for x in a]
    b = [int(x) for x in b]

    xx = [0] * n 
    yy = [0] * n

    zx = 0
    ox = 0
    zy = 0
    oy = 0

    for i in range(n):
        if a[i] == 0:
            zx += 1
        else:
            ox += 1

        if b[i] == 0:
            zy += 1
        else:
            oy += 1

        if i == 0:
            xx[i] = 1
            yy[i] = 1
        else:
            xx[i] = abs(zx - ox)
            yy[i] = abs(zy - oy)

    for i in range(1,n):
        xx[i] += xx[i-1]
        yy[i] += yy[i-1]

    PRI(xx)
    PRI(yy)
    ans = 0
    for i in range(n):
        ans += xx[i] - xx[i-1] if i > 0 else xx[i]
        ans += yy[n - 1]

    for i in range(n):
        ans += yy[i] - yy[i-1] if i > 0 else yy[i]
        ans += xx[n - 1]    

    PRI(ans)
    

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
