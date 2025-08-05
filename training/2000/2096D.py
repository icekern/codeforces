# title: 2096D.py
# author: firekern
# date: 2025-08-05 22:06:38
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
    x = []
    z = []
    for i in range (n):
        a,b = LI()
        c = a + b
        x.append(a)
        z.append(c)
    
    x.sort()
    z.sort()
    buld_x = None
    buld_z = None
    for i in range (0, n-1, 2):
        if x[i] != x[i + 1]:
            buld_x = x[i]
            break
    if buld_x == None:
        buld_x = x[-1]
    for i in range (0, n-1, 2):
        if z[i] != z[i + 1]:
            buld_z = z[i]
            break
    if buld_z == None:
        buld_z = z[-1]
        
    PRI(buld_x, buld_z - buld_x)
    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
