# title: 2065D.py
# author: firekern
# date: 2025-08-15 23:29:35
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

    n, m = II()
    ll = [LI() for _ in range(n)]

    ll.sort(key=lambda x: sum(x), reverse=True)

    c = [0] * (n * m)
    c[0] = ll[0][0]

    for i in range(1, n * m):
        c[i] = c[i - 1] + ll[i // m][i % m]

    sol = c[0]
    for i in range(1, n * m):
        sol += c[i]

    PRI(sol)


def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
