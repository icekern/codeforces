# Created on: 11/07/2025 19:23:13
# Author: Porcelli
# GitHub: https://github.com/icekern/codeforces

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
    a = LI()
    b = LI()

    mod = 998244353

    mas_pfx_a = [(0,0)] * (n)
    mas_pfx_b = [(0,0)] * (n)

    mas_pfx_a[0] = (a[0],0)
    mas_pfx_b[0] = (b[0],0)
    

    for i in range(1,n):
        if a[i] > mas_pfx_a[i-1][0]:
            mas_pfx_a[i] = (a[i], i)
        else:
            mas_pfx_a[i] = mas_pfx_a[i-1]
            
        if b[i] > mas_pfx_b[i-1][0]:
            mas_pfx_b[i] = (b[i], i)
        else:
            mas_pfx_b[i] = mas_pfx_b[i-1]

    r = []
    for i in range(n):

        if mas_pfx_a[i][0] > mas_pfx_b[i][0]:
            r.append(pow(2, mas_pfx_a[i][0], mod) + pow(2, b[i - mas_pfx_a[i][1]], mod))
        elif mas_pfx_b[i][0] > mas_pfx_a[i][0]:
            r.append(pow(2, mas_pfx_b[i][0], mod) + pow(2, a[i - mas_pfx_b[i][1]], mod))
        else:
            if a[i - mas_pfx_b[i][1]] <= b[i - mas_pfx_a[i][1]]:
                r.append(pow(2, mas_pfx_a[i][0], mod) + pow(2, b[i - mas_pfx_a[i][1]], mod))
            else:
                r.append(pow(2, mas_pfx_b[i][0], mod) + pow(2, a[i - mas_pfx_b[i][1]], mod))

        r[i] %= mod
    
    PRI(*r)


def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()