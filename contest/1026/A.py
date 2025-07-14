# Created on: 14/07/2025 14:16:03
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


    max_val = max(a)
    min_val = min(a)

    if (max_val + min_val) % 2 == 0:
        PRI(0)
    else:
        c_sort = [0] * (51)

        for i in range(n):
            c_sort[a[i]] += 1

        sol = 100
        cost = 0
        for i in range(min_val, max_val + 1):
            if min_val % 2 == i % 2:
                cost += c_sort[i]
            elif c_sort[i] > 0:
                sol = min(sol, cost)
                break

        cost = 0
        for i in range(max_val, min_val - 1, -1):
            if max_val % 2 == i % 2:
                cost += c_sort[i]
            elif c_sort[i] > 0:
                sol = min(sol, cost)
                break

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