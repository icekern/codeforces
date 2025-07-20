# Created on: 20/07/2025 18:06:44
# Author: Porcelli
# GitHub: https://github.com/icekern/codeforces

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
    n,m = II()
    a = LI()
    b = LI()


    prefix = [-1] * m
    suffix = [-1] * m

    idx = 0 
    for i in range(n):
        if idx <= m - 1 and a[i] >= b[idx]:
            prefix[idx] = i 
            idx += 1

    idx = m - 1
    for i in range(n - 1, -1, -1):
        if idx >= 0 and a[i] >= b[idx]:
            suffix[idx] = i
            idx -= 1


    sol = int(1e13)
    for i in range(m):

        l = prefix[i - 1] if i > 0 else -2
        r = suffix[i + 1] if i < m - 1 else n

        if l < r and l != -1 and r != -1:
            sol = min(sol,b[i])

    if prefix[m - 1] != -1:
        sol = 0    

    if sol == int(1e13):
        sol = -1 

    PRI(sol)


def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()