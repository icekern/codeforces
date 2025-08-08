# title: 1231C.py
# author: firekern
# date: 2025-08-08 16:27:45
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
    # observations

    # i have a matrix with 0 where i can place whatever i want
    # find the max(sum(mat)) where mat is increasing
    # the row are in increasing order 
    # the columns are in increasing order
    # a reverse cycle


    n,m = II()
    mat = [LI() for _ in range(n)]

    for j in range(m - 2, -1, -1):
        for i in range(n - 2, -1, -1):
            if mat[i][j] == 0:
                mat[i][j] = min(mat[i + 1][j], mat[i][j + 1]) - 1
            else:
                if mat[i][j] > min(mat[i + 1][j], mat[i][j + 1]) - 1:
                    PRI(-1)
                    return
                
    PRI(sum(sum(row) for row in mat))
                
    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
