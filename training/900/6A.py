# title: 2102A.py
# author: firekern
# date: 2025-07-25 21:35:09
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
    a = LI()
    a.sort()

    if a[0] + a[1] < a[2] and a[2] + a[1] < a[3]:
        PRI("IMPOSSIBLE")
    elif a[0] + a[1] > a[2] or a[2] + a[1] > a[3]:
        PRI("TRIANGLE")
    elif a[0] + a[1] == a[2] or a[2] + a[1] == a[3]:
        PRI("SEGMENT")
    
    
    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
