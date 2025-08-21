# title: 1926B.py
# author: firekern
# date: 2025-08-16 19:57:55
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
    g = [input() for _ in range(n)]
    r1, r2 = n, -1
    c1, c2 = n, -1
    for i in range(n):
        for j, ch in enumerate(g[i]):
            if ch == '1':
                if i < r1: r1 = i
                if i > r2: r2 = i
                if j < c1: c1 = j
                if j > c2: c2 = j

    h = r2 - r1 + 1
    w = c2 - c1 + 1
    if h == w:
        print("SQUARE")
    else:
        print("TRIANGLE")


            
                        

    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
