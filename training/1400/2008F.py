# Created on: 16/07/2025 11:05:01
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
MOD = 10**9 + 7

def modinv(a, m):
    return pow(a, m - 2, m)

def solve():

    n = I()
    a = LI()

    tot_sum = sum(a)
    numerator = 0
    denominator = n

    for i in range(n):
        tot_sum -= a[i]
        numerator += a[i] * (tot_sum)
        numerator %= MOD
        
    result = (numerator * pow(((denominator - 1) * (denominator) * pow(2,-1,MOD)) % MOD,-1,MOD)) % MOD

    PRI(result)

    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()