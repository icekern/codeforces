# title: 2065C1.py
# author: firekern
# date: 2025-08-15 17:32:31
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

    n,m =  II()
    a = LI()
    b = LI()

    c = [0] * n
    c[0] = b[0] - a[0] if b[0] - a[0] <= a[0] else a[0]

    for i in range(1,n):
        val = 0

        if b[0] - a[i] <= a[i]:
            if b[0] - a[i] >= c[i-1]:
                val = b[0] - a[i]
            else:
                val = a[i]
        else:
            if a[i] >= c[i-1]:
                val = a[i]
            else:
                val = b[0] - a[i]

        if val >= c[i-1]:
            c[i] = val
        else:
            PRI("NO")
            return
    PRI("YES")
        


def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
