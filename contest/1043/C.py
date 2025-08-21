# title: C.py
# author: firekern
# date: 2025-08-21 16:59:39
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
    n,m = II()
    nn = n

    l = []

    while nn > 0:
        l.append(nn % 3)
        nn //= 3

    for i in range(len(l)):
        m -= l[i]

    if m < 0:
        PRI(-1)
        return

    for i in range(len(l) - 1, 0, -1):
        k = l[i]
        to_remove = min(m//2,k)
        m -= to_remove * 2
        l[i] -= to_remove
        l[i - 1] += 3 * to_remove
            
    sol = 0

    for i in range(len(l)):
        sol += l[i] * (int(pow(3, i + 1)) + i * int(pow(3, i - 1)))

    PRI(sol)

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
