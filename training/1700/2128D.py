# Created on: 2025-07-28 18:27

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

# https://github.com/icekern/codeforces

DEBUG = 1
MULTI = True

# i have a permutation of n elements
# i need to calculate the lenght for every 
# l,r of the longst increasing subsequence

# complexity searched is O(n) or O(n log n)
# condition 1 
# for every i, i + 1 
# max(p[i], p[i + 1]) > p[i + 2]

# observation 1
# min sequence is i choose to take the maximum between the pairs of elements
# at min n // 2
# if i have that 
# 1 > 2 > 3 ok 
# 1 > 3  ok 
# O(n)
# increasing subsequnce 
# 
# 1 1 0 1 0 1 0 1 0 1
# observation 2 
# case 1 
# sol += n 
# case 2 
# sol += pairs 
# case x >= 3
# sol += the segment (l,r)
# we know (2)

# 70 68     
# the sequence is like this 

# 1 1 1 1 1 1 0 1 0 1 0 1

# if the sequence end in 0 + 1

# so the solutions is 

# calculate dp[i] = 1 if it is part of LDS
# 0 otherwise

# let i be the index that we are analyzing
# sol += pfx[everything after i]
# this pfx is the prefix sum of dp + 1 iff
# that index ends in 0 

# brosky balosky melosky


def solve():

    n = I()
    a = LI()

    dp = [0] * n
    pfx = [0] * (n + 1)

    if a[0] > a[1]:
        dp[0] = 1
    else:
        dp[1] = 1

    for i in range(1,n):
        if a[i] == a[i - 1] - 1 or a[i] == a[i - 2] - 1:
            dp[i] = 1
        else:
            dp[i] = 0


    for i in range(n - 1, -1, -1):
        pfx[i] = pfx[i + 1] + dp[i]

    sol = 0
    for i in range(n):
        for j in range(i + 1, n):
            sol += pfx[j]


    print(sol)

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()