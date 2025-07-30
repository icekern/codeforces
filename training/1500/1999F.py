# title: 1999F.py
# author: firekern
# date: 2025-07-30 15:53:04
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
MOD = int(1e9 + 7)

def solve():

    n,k = II()
    a = LI()
    o = 0
    sol = 0

    factorial = [1] * (n + 1)
    for i in range(2, n + 1):
        factorial[i] = (factorial[i - 1] * i) % MOD

    def binomial(n, k):
        if k > n or k < 0:
            return 0
        return (factorial[n] * pow(factorial[k], MOD - 2, MOD) * pow(factorial[n - k], MOD - 2, MOD)) % MOD
 
    for i in range(n):
        o += a[i] % 2 

    for i in range(k // 2 + 1, o + 1):
        sol += binomial(o, i) * binomial(n - o, k - i)
        sol %= MOD 

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
