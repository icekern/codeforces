# title: B.py
# author: firekern
# date: 2025-09-13 10:06:04
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

DEBUG = 0
MULTI = True 

def solve():


    n = I()
    a = LI()

    a.sort()

    solx = 0
    soly = 0

    for i in range(1,n,2):
        solx += a[i]

    if n % 2 == 1:
        solx += a[-1]

    for i in range(n - 1, 0, -2):
        soly += a[i]

    if n % 2 == 1:
        soly += a[0]

    PRI(min(solx, soly))



def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
