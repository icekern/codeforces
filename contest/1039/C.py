# title: C.py
# author: firekern
# date: 2025-07-22 16:33:08
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

DEBUG = 0
MULTI = True 

pfx = [0] * 210
primes = [2,3,5,7]

for i in primes:
    for j in range(i,210,i):
        pfx[j] = 1

pfx[0] = 1
for i in range(1,len(pfx)):
    pfx[i] += pfx[i - 1]


def solve():
    a,b = II()
    
    r_a = a % 210
    r_b = b % 210 

    cycle_a = a // 210
    cycle_b = b // 210

    sol = 0

    if cycle_a == cycle_b:
        sol = pfx[r_b] - (pfx[r_a - 1] if r_a != 0 else 0)
    else:
        sol = pfx[r_b] + (pfx[209] - (pfx[r_a - 1] if r_a != 0 else 0)) \
                       + (cycle_b - 1 - cycle_a) * pfx[209]

        
    PRI((b - a + 1) - sol)

    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()