# title: 1567C.py
# author: firekern
# date: 2025-07-30 12:10:09
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
    n = input().strip()[::-1]
    len_n = len(str(n))

    dp = [[0,0,0] for _ in range(len_n + 1)]
    moves = [9,8,7,6,5,4,3,2,1,0]

    dp[0][0] = int(n[0]) + 1
    dp[0][1] = 0
    dp[0][2] = moves[int(n[0])]
    
    if len_n == 1:
        PRI(dp[0][0] - 2)
        return
    
    dp[1][0] = dp[0][0] * (int(n[1]) + 1) + dp[0][1] * int(n[0])
    dp[1][1] = dp[0][2] * (int(n[1]) + 1)
    dp[1][2] = moves[int(n[1])] + (dp[0][1] * 9 if int(n[1]) == 0 else 0)

    for i in range(2, len_n):
        dp[i][0] = dp[i-1][0] * (int(n[i]) + 1) + dp[i-1][1] * (int(n[i]) + 1 if i != len_n - 1 else int(n[i]))
        dp[i][1] = dp[i-1][2] * (int(n[i]) + 1)
        dp[i][2] = moves[int(n[i])] + (dp[i-1][1] * 9 if int(n[i]) == 0 else 0)

    PRI(dp)
    PRI(dp[len_n - 1][0] - 2)

    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()
 
if __name__ == '__main__':
    main()
