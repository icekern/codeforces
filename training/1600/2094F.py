# Created on: 20/07/2025 10:09:11
# Author: Porcelli
# GitHub: https://github.com/icekern/codeforces

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
    n,m,k = II()

    mat = [[0 for _ in range(m)] for _ in range(n)]


    if m % k != 0:
        s = 0
        for i in range(n):
            for j in range(m):
                mat[i][j] = s % k
                s += 1
    else:
        s = 0
        for i in range(n):
            for j in range(m):
                if i % 2 == 0:
                    mat[i][j] = s % k
                else:
                    mat[i][m - j - 1] = (k - s) % k
                s += 1

    for i in range(n):
        for j in range(m):
            PRI(mat[i][j] + 1, end=' ')
        PRI()

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()