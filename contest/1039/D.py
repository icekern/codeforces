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

DEBUG = 1
MULTI = False
MOD = 998244353

def solve():

    n,m = II()
    segments = [LI() for _ in range(n)]
    dp = [0 for _ in range(m + 1)]
    segments.sort()

    dp[0] = 1
    ppfx = [1] * (m + 1)

    k = 0
    for i in range(1,m + 1):
        while k <= n - 1 and i == segments[k][0]:
            ppfx[i] *= (segments[k][3] - segments[k][2]) * pow(segments[k][3], -1, MOD)
            ppfx[i] %= MOD
            k += 1
        ppfx[i] *= ppfx[i - 1]
        ppfx[i] %= MOD
    k = 0
    
    for i in range(1,m + 1):
        while k <= n - 1 and i == segments[k][0]:
            l,r,p,q = segments[k]
            dp[r] += dp[l - 1] * p * pow(q,-1,MOD) * pow(ppfx[l - 1], -1, MOD) * ppfx[r] * pow((q - p) * pow(q,-1,MOD), -1 , MOD)
            dp[r] %= MOD
            k += 1

    PRI(dp[m])

    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
