# title: D.py
# author: firekern
# date: 2025-07-22 16:33:11
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
MOD = 998244353

def solve():

    n,m = II()
    segments = [II() for _ in range(n)]
    dp = [[0,0] for _ in range(m + 2)]
    segments.sort()

    k = 0
    dp[1] = [1,1]
    for i in range(1,m):
        while k < n and segments[k][0] == i:
            dp[segments[k][1] + 1][0] += dp[i][0] * segments[k][2]
            dp[segments[k][1] + 1][0] %= MOD
            dp[segments[k][1] + 1][1] += dp[i][1] * segments[k][3]
            dp[segments[k][1] + 1][1] %= MOD

            k += 1

    PRI(dp[m + 1])

    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
