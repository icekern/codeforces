# Created on: 13/07/2025 11:52:11
# Author: Porcelli
# GitHub: https://github.com/icekern/codeforces

import sys
from collections import defaultdict, deque, Counter
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
MULTI = False 

def solve():

    n = int(input())
    point = [[int(i) for i in input().split()] for _ in range(4 * n + 1)]
    
    countX = Counter(map(lambda a: a[0], point))
    countY = Counter(map(lambda a: a[1], point))
    
    x = [a for a in countX if countX[a] >= n]
    y = [a for a in countY if countY[a] >= n]
    
    sX = (min(x), max(x))
    sY = (min(y), max(y))
    
    for p in point:
        if not ((p[0] in sX and sY[0] <= p[1] <= sY[1]) or (p[1] in sY and sX[0] <= p[0] <= sX[1])):
            print(*p)

    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()