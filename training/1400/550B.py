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


def solve():
    # n problems
    # i-th problem has a difficulty of c_i
    # problemset |s| > 2 Vp  l <= sum(p) <= r  max(P) - min(P) >= x
    # find the number of ways to choose a problemset for the contest 
    # solve with brute force

    n, l, r, x = II()
    p = LI()

    p.sort()
    sol = 0

    for i in range(1 << n):
        s = []
        sum_s = 0
        max_s = -1
        min_s = 1 << 30
        
        for j in range(n):
            if i & (1 << j):
                sum_s += p[j]
                max_s = max(max_s, p[j])
                min_s = min(min_s, p[j])

        if l <= sum_s <= r and max_s - min_s >= x:
            sol += 1

    print(sol)


def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

MULTI = False 
if __name__ == '__main__':
    main()