# title: 2084D.py
# author: firekern
# date: 2025-08-08 16:40:03
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
    n, m, k = II()

    # given an array of n elements 
    # u can remove a subarray of size k
    # m times
    # find a t.c f(f(...f(a))) is maximized
    
    # observations 
    # if i can remove 1 2 3 

    sol = []
    r = n // (m + 1)
    for i in range(n):
        sol.append(i % r)
        
    PRI(*sol)

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
