# title: 2110.py
# author: firekern
# date: 2025-07-23 19:46:25
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

    n,m = II()
    b = LI()
    edges = [LI() for _ in range(m)]

    graph = defaultdict(list)
    l,r = 0,int(1e20)
    sol = -1

    for e in edges:
        u,v,w = e
        graph[u].append((v,w))

    while l <= r:
        mid = (l + r) // 2 
        dp = [-int(1e12)] * (n + 1)
        dp[1] = 0

        for i in range(1,n):
            if dp[i] == -int(1e12):
                continue
            dp[i] += b[i - 1]
            dp[i] = min(dp[i],mid)
            for x,w in graph[i]:
                if dp[i] >= w:
                    dp[x] = max(dp[x],dp[i])
        
        if dp[n] == -int(1e12):
            l = mid + 1
        else:
            sol = mid
            r = mid - 1 

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
