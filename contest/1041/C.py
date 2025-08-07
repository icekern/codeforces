# title: C.py
# author: firekern
# date: 2025-08-07 16:15:52
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
    a,b = LI(), LI()

    k = [(i,j) for i,j in zip(a,b)]

    k.sort(key=lambda x: x[0])

    sol = int(1e9)
    j = 0
    for i in range(n - 1):
        r = [k[i][0], k[i][1], k[i + 1][0], k[i + 1][1]]
        r.sort()
        contribute = abs(k[i + 1][0] - k[i + 1][1]) + abs(k[i][1] - k[i][0])
        if sol > (r[3] - r[0] + r[2] - r[1]) - contribute:
            sol = (r[3] - r[0] + r[2] - r[1]) - contribute
            j = i

    solz = 0
    for i in range(n):
        if i == j or i == j + 1:
            continue
        solz += abs(k[i][1] - k[i][0])

    f = [k[j][0], k[j][1], k[j + 1][0], k[j + 1][1]]
    f.sort()
    solz += f[3] - f[0] + f[2] - f[1]

    PRI(solz)

    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
