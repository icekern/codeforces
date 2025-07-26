# title: 2003D1.py
# author: firekern
# date: 2025-07-26 20:44:35
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
    a = [LI() for _ in range(n)]
    mexs = [[0,0] for _ in range(n)]

    for i in range(n):
        a[i].sort()
        len_a = len(a[i])
        j = 0
        mex = 0
        
        while j < len_a:
            while a[i][j] == mex:
                j += 1
                

            j += 1

    graph = defaultdict(list)

    PRI(mexs)

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
