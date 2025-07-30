# title: 1999G1.py
# author: firekern
# date: 2025-07-30 16:21:47
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
MULTI = True 

def solve():
    l, r = 1, 1000
    while l <= r:
        mid = (l + r) // 2
        PRI(f"? {mid} 1", flush=True)

        if I() == mid:
            l = mid + 1
        else:
            r = mid - 1
    
    PRI(f"! {l}", flush=True)

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
