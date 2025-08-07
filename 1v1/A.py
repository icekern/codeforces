# title: A.py
# author: firekern
# date: 2025-08-06 11:29:48
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
    v = LI()

    p = False
    for i in range(1,n):
        if v[i] != v[i-1]:
            p = True

    m = max(v)
    if p:
        PRI('YES')
        sol = []
        for i in range(n):
            if v[i] == m:
                sol.append(1)
            else:
                sol.append(2)

        PRI(*sol)
                
    else:
        PRI('NO')

            

    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
