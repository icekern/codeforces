# title: A.py
# author: firekern
# date: 2025-08-07 16:15:48
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
    a = LI()

    setz = set()
    for i in range(n):
        if a[i] != -1:
            setz.add(a[i])
        
    if len(setz) == 1 or len(setz) == 0:
        e = setz.pop() if setz else 1
        if e == 0:
            PRI('NO')
        else:     
            PRI('YES')
    else:
        PRI('NO')

    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
