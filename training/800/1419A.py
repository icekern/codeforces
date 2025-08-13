# title: 1419A.py
# author: firekern
# date: 2025-08-13 23:24:34
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
    a = [int(x) for x in a]
    raze = [0,0]
    breach = [0,0]

    for i in range(n):
        if i % 2 == 0:
            raze[a[i] % 2] += 1
        else:
            breach[a[i] % 2] += 1

    if n % 2 == 1:
        if raze[1] >= 1:
            PRI(1)
        else:
            PRI(2)
    else:
        if breach[0] >= 1:
            PRI(2)
        else:
            PRI(1)

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
