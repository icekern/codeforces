# Created on: 14/07/2025 14:42:30
# Author: Porcelli
# GitHub: https://github.com/icekern/codeforces

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

    segments = [LI() for _ in range(n)]

    pfx_sum = [0] * (n)

    pfx_sum[0] = a[0] if a[0] >= 0 else 0

    for i in range(1,n):
        if a[i] >= 0:
            pfx_sum[i] = pfx_sum[i - 1] + a[i]
        else:
            pfx_sum[i] = pfx_sum[i - 1]

    min_max_high = [0] * (n)
    min_max_high[n - 1] = segments[n - 1][1] - pfx_sum[n - 1]

    for i in range(n - 2, -1, -1):
        min_max_high[i] = min(min_max_high[i + 1], segments[i][1] - pfx_sum[i])

    actual_high = 0
    flag = True

    for i in range(n):

        if a[i] < 0:
            if actual_high + 1 - pfx_sum[i] <= min_max_high[i]:
                a[i] = 1
            else:
                a[i] = 0
        
        actual_high += a[i] if a[i] >= 0 else 0
        if not (segments[i][0] <= actual_high <= segments[i][1]):
            flag = False
            break

    if flag:
        PRI(*a)
    else:
        PRI(-1)
    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()