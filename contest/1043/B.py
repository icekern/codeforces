# title: B.py
# author: firekern
# date: 2025-08-21 16:38:20
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
    
    peppe = []
    k = 1
    while True:
        giuseppe = 1 + 10**k
        if giuseppe > n:
            break
        if n % giuseppe == 0:
            x = n // giuseppe
            peppe.append(x)
        k += 1

    peppe.sort()
    PRI(len(peppe))
    PRI(*peppe)


def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
