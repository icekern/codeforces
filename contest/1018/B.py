# title: B.py
# author: firekern
# date: 2025-08-03 22:19:24
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
    lg = LI()
    rg = LI()

    sol = 0
    smallest_e = []
    for i in range(n):
        sol += max(lg[i], rg[i])
        smallest_e.append(min(lg[i], rg[i]))

    smallest_e.sort(reverse=True)
    for i in range(k - 1):
        sol += smallest_e[i]

    sol += 1

    PRI(sol)
        

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
