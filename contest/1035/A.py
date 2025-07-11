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
    a,b,x,y = II()

    sol = 0
    if a > b:
        if a ^ 1 == b:
            sol = y
        else:
            sol = -1
    else:
        dp = [int(1e18) for _ in range(b + 1)]
        dp[a] = 0

        for i in range(a, b + 1):
            if i ^ 1 <= b:
                dp[i ^ 1] = min(dp[i ^ 1], dp[i] + y)
            if i + 1 <= b:
                dp[i + 1] = min(dp[i + 1], dp[i] + x)

        sol = dp[b]

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
