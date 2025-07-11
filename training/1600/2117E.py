# Created on: 11/07/2025 18:10:46
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

# this code doesn t work cuz they like to do testcase to brust python dictonary

def solve():
    n = I()
    a = LI()
    b = LI()

    first_strip = defaultdict(list)
    second_strip = defaultdict(list)

    for i in range(n - 1, -1, -1):
        first_strip[a[i] if i % 2 == 1 else b[i]].append(i)
        second_strip[b[i] if i % 2 == 1 else a[i]].append(i)

    sol = 0
    for i in range(1,n + 1):
        if first_strip[i] and second_strip[i]:
            sol = max(sol, min(first_strip[i][0], second_strip[i][0]) + 1)
        
        if len(first_strip[i]) > 1:
            if first_strip[i][0] == first_strip[i][1] + 1:
                if len(first_strip[i]) > 2:
                    sol = max(sol, first_strip[i][2] + 1)
            else:
                sol = max(sol, first_strip[i][1] + 1)

        if len(second_strip[i]) > 1:
            if second_strip[i][0] == second_strip[i][1] + 1:
                if len(second_strip[i]) > 2:
                    sol = max(sol, second_strip[i][2] + 1)
            else:
                sol = max(sol, second_strip[i][1] + 1)

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