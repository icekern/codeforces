# title: 1990C.py
# author: firekern
# date: 2025-07-29 17:24:01
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
    a = LI()

    count = [0] * (n + 1)
    b = []
    mas = 0

    for i in range(n):
        count[a[i]] += 1
        if count[a[i]] >= 2 and a[i] > mas:
            mas = a[i]
        b.append(mas)

    count = [0] * (n + 1)
    c = []
    mas = 0

    for i in range(n):
        count[b[i]] += 1
        if count[b[i]] >= 2 and b[i] > mas:
            mas = b[i]
        c.append(mas)


    sol = sum(a) + sum(b)
    for i in range(n):
        sol += c[i] * (n - i)
        
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
