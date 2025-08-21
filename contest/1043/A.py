# title: A.py
# author: firekern
# date: 2025-08-21 16:34:13
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
    s = [c for c in input().strip()]
    m = I()
    ss = [c for c in input().strip()]
    direction = [c for c in input().strip()]

    right = []
    left = []

    for i in range(m):
        if direction[i] == 'D':
            right.append(ss[i])
        else:
            left.append(ss[i])
    
    PRI(''.join(left[::-1]) + ''.join(s) + ''.join(right))

    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
