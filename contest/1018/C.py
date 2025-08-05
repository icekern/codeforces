# title: C.py
# author: firekern
# date: 2025-08-03 22:37:26
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

def check_if_at_the_same_index_are_equal(a, b):
    return any(a[i] == b[i] for i in range(len(a)))

def solve():

    n = I()

    mat = [LI() for _ in range(n)]

    b = LI()
    a = LI()

    dpr = [[10**18,10**18] for _ in range(n)]
    dpc = [[10**18,10**18] for _ in range(n)]


    dpr[0][0] = 0
    dpr[0][1] = b[0]
    dpc[0][0] = 0
    dpc[0][1] = a[0]

    for i in range(1,n):

        x = mat[i]
        y = mat[i-1]
        y1 = [k + 1 for k in y]
        x1 = [k + 1 for k in x]

        if not check_if_at_the_same_index_are_equal(x, y):
            dpr[i][0] = min(dpr[i][0],dpr[i-1][0])
        if not check_if_at_the_same_index_are_equal(x, y1):
            dpr[i][0] = min(dpr[i][0],dpr[i-1][1])
        if not check_if_at_the_same_index_are_equal(x1, y):
            dpr[i][1] = min(dpr[i][1],dpr[i-1][0] + b[i])
        if not check_if_at_the_same_index_are_equal(x1, y1):
            dpr[i][1] = min(dpr[i][1],dpr[i-1][1] + b[i])

    reflected = [[] for _ in range(n)]

    for i in range(n):
        reflected[i] = [mat[j][i] for j in range(n)]
    
    for i in range(1,n):

        x = reflected[i]
        y = reflected[i-1]
        y1 = [k + 1 for k in y]
        x1 = [k + 1 for k in x]

        if not check_if_at_the_same_index_are_equal(x, y):
            dpc[i][0] = min(dpc[i][0],dpc[i-1][0])
        if not check_if_at_the_same_index_are_equal(x, y1):
            dpc[i][0] = min(dpc[i][0],dpc[i-1][1])
        if not check_if_at_the_same_index_are_equal(x1, y):
            dpc[i][1] = min(dpc[i][1],dpc[i-1][0] + a[i])
        if not check_if_at_the_same_index_are_equal(x1, y1):
            dpc[i][1] = min(dpc[i][1],dpc[i-1][1] + a[i])


    if min(dpr[n-1]) == 10**18 or min(dpc[n-1]) == 10**18:
        PRI(-1)
    else:
        PRI(min(dpr[n-1]) + min(dpc[n-1]))

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
