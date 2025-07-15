# Created on: 15/07/2025 14:31:20
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
    n, q  = II()
    a = LI()
    queries = [ LI() for _ in range(q) ]

    prefix = [0] * n
    prefix[0] = a[0]

    for i in range(1, n):
        prefix[i] = prefix[i - 1] + a[i]

    def calculate_sum(l, r):
        if l <= r:
            return prefix[r] - (prefix[l - 1] if l > 0 else 0)
        else:
            return prefix[n - 1] - (prefix[l - 1] if l > 0 else 0) + prefix[r]
    
    for l, r in queries:

        first_segment = (l - 1) // n
        second_segment = (r - 1) // n

        if first_segment != second_segment:
            partial_sum = (second_segment - first_segment - 1) * prefix[-1]
        else:
            partial_sum = 0
            
        idx_l = ((l - 1) % n + first_segment) % n
        idx_r = ((r - 1) % n + second_segment) % n

        if first_segment == second_segment:
            partial_sum += calculate_sum(idx_l, idx_r)
        else:
            partial_sum += calculate_sum(idx_l, (n - 1 + first_segment) % n)
            partial_sum += calculate_sum(second_segment, idx_r)

        PRI(partial_sum)
    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()