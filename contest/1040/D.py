# title: D.py
# author: firekern
# date: 2025-07-27 17:16:53
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

    dp = [0] * n
    fz = [(i + 1) for i in range(n)]
    seen = [False] * (n + 1)

    for i in range(n):

        while seen[fz[-1]] == True:
            fz.pop() 

        if a[i] == fz[-1]:
            dp[i] = 1
            fz.pop()
            seen[a[i]] = True
        else:
            seen[a[i]] = True
            dp[i] = 0

    p_sum = sum(dp)
    t_sum = p_sum

    for i in range(n):
        p_sum -= dp[i] 
        t_sum += p_sum
    
    sol = 0
    for i in range(n - 1, -1, -1):
        sol += t_sum + (i + 1 if dp[i] == 0 else 0)
        t_sum -= dp[i] * (i + 1)
    PRI(sol)

    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
