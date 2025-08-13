# title: C.py
# author: firekern
# date: 2025-08-10 16:45:41
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
    a = LI()
    b = LI()
    c = []
    d = []

    for i in range(n):
        c.append(min(a[i] % k, k - a[i] % k))
        d.append(min(b[i] % k, k - b[i] % k))
        
    c.sort()
    d.sort()
    for i in range(n):
        if c[i] != d[i]:
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
