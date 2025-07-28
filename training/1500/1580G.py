# title: 1580G.py
# author: firekern
# date: 2025-07-28 23:07:20
# github: https://github.com/icekern/codeforces

import sys
from collections import defaultdict, deque
import math
import heapq
import bisect
import random

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

    vertical = defaultdict(int)
    horizontal = defaultdict(int)
    diagonal_neg = defaultdict(int)
    diagonal_pos = defaultdict(int)
    
    n = I()
    points = [LI() for _ in range(n)]
    points = points[::-1]
    random.shuffle(points)

    for p in points:
        vertical[p[0]] += 1
        horizontal[p[1]] += 1
        diagonal_neg[p[0] - p[1]] += 1
        diagonal_pos[p[0] + p[1]] += 1

    sol = 0
    for x in vertical:
        sol += vertical[x] * (vertical[x] - 1)
    for x in horizontal:
        sol += horizontal[x] * (horizontal[x] - 1)
    for x in diagonal_neg:
        sol += diagonal_neg[x] * (diagonal_neg[x] - 1)
    for x in diagonal_pos:
        sol += diagonal_pos[x] * (diagonal_pos[x] - 1)

    PRI(sol)




def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
