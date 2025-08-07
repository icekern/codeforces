# title: B.py
# author: firekern
# date: 2025-08-06 11:43:17
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

    mat = [[c for c in input()] for _ in range(n)]

    rows = []
    for i in range(n):
        rows.append((mat[i].count('#'), i))

    rows.sort(reverse=True)
    x = rows[0][1]


    start,end = -1, -1
    for i in range(m):
        if mat[x][i] == '#'and start == -1:
            start = i     
        if mat[x][i] == '#' and end < i:
            end = i

    PRI(x + 1, start + (end - start) // 2  + 1)
        


def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
