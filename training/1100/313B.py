# title: 313B.py
# author: firekern
# date: 2025-08-05 17:05:12
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

DEBUG = 0
MULTI = False

def solve():
    s = input().strip()
    n = len(s)

    s = s + '1'
    
    q = I()
    pfx = [0] * (n + 1)
    for i in range(0,n):
        if i > 0:
            pfx[i] = pfx[i - 1] + (1 if s[i + 1] == s[i] else 0)
        else:
            pfx[i] = (1 if s[i + 1] == s[i] else 0)

    for i in range(q):
        l,r = LI()
        PRI((pfx[r - 2] if r - 2 >= 0 else 0) - (pfx[l - 2] if l - 2 >= 0 else 0))

    

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
