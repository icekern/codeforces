# title: 1774B.py
# author: firekern
# date: 2025-07-28 23:23:57
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

    n,m,k = LI()
    a = LI()

    # k is the period
    # when the period is violated
    
    max_paint = n // k 
    paint_residue = n % k 

    flag = "YES"
    for i in range(m):
        if a[i] > max_paint:
            if a[i] == max_paint + 1 and paint_residue > 0:
                paint_residue -= 1
            else:
                flag = "NO"


    PRI(flag)




    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
