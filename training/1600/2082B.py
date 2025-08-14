# title: 2082B.py
# author: firekern
# date: 2025-08-14 16:38:14
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

    x,n,m = II()
    
    xx,nn,mm = x, n, m
    while xx > 0 and nn + mm > 0:
        if xx == 1:
            if nn == 0:
                xx = 1
            else:
                xx = 0
            break

        if nn > 0:
            xx //= 2
            nn -= 1
        else:
            xx = (xx + 1) // 2
            mm -= 1

    q = xx 

    xx,nn,mm = x, n, m
    while xx > 0 and nn + mm > 0:
        if xx == 1:
            if nn == 0:
                xx = 1
            else:
                xx = 0
            break

        if mm > 0:
            xx = (xx + 1) // 2
            mm -= 1
        else:
            xx //= 2
            nn -= 1

    qq = xx

    PRI(qq,q)



            
        

        

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
