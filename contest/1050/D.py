# title: D.py
# author: firekern
# date: 2025-09-13 16:57:19
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

    even = [ e for e in a if e % 2 == 0]
    odd = [ e for e in a if e % 2 == 1]

    even.sort()
    odd.sort(reverse=True)

    sol = 0
    for i in range(len(odd) // 2 + len(odd) % 2):
        sol += odd[i]

    if sol == 0:
        PRI(sol)
    else:
        sol += sum(even)
        PRI(sol)

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
