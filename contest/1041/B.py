# title: B.py
# author: firekern
# date: 2025-08-01 16:22:52
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
    n, k = II()
    a = LI()

    z = a.count(0)
    o = a.count(1)
    t = a.count(2)

    sol = [0 for _ in range(z)]

    for i in range(max(t, o)):
        if i < t:
            sol.append(2)
        if i < o:
            sol.append(1)

    if k >= sum(a):
        k -= sum(a)

        for i in range(200):
            if (k - i * 3) % 2 == 0 and k >= i * 3:
                sol = [-1]


    PRI(*sol)

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
