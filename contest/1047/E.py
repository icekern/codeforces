# title: E.py
# author: firekern
# date: 2025-09-07 17:11:29
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
MULTI = True 

def simulate(a):

    c_sort = [0] * (len(a) + 1)
    for i in range(len(a)):
        c_sort[a[i]] += 1

    mex = 0
    for i in range(len(a) + 1):
        if c_sort[i] > 0:
            mex = i + 1
        else:
            break
    
    for i in range(len(a)):
        if c_sort[a[i]] > 1 and a[i] < mex:
            a[i] = mex
        
        if a[i] > mex:
            a[i] = mex

    return a

def solve():
    n,k = II()
    a = LI()
    dp = [0,0]

    a = simulate(a)
    dp[0] = sum(a)
    a = simulate(a)
    dp[1] = sum(a)
    if k >= 2:
        a = simulate(a)
        dp[0] = sum(a)

    PRI(dp[0] if k % 2 == 1 else dp[1])

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
