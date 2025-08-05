# title: 2021B.py
# author: firekern
# date: 2025-08-04 19:51:43
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
    n,x = II()
    a = LI()
    a.sort()

    b = [a[0]]
 
    for i in range(1,n):
        if a[i] == a[i-1]:
            b.append(a[i] + x)
        else:
            b.append(a[i])

    b.sort()

    mex = 0
    for i in range(n):
        if b[i] == mex:
            mex += 1
        elif b[i] > mex:
            break

    PRI(mex)

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
