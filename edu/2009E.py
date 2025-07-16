# Created on: 16/07/2025 10:09:28
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

    n,k = LI()

    # ternary search over val

    def val(mid):
        val1 = (mid+k-1+k)*mid//2
        val2 = (k+n-1+k)*n//2 - val1
        return abs(val1 - val2)
    
    lo, hi = 1, n
    
    while lo < hi:
        mid1 = lo + (hi - lo) // 3
        mid2 = hi - (hi - lo) // 3
        val1 = val(mid1)
        val2 = val(mid2)
        
        if val1 < val2:
            hi = mid2 - 1
        else:
            lo = mid1 + 1
        
    PRI(val(lo))

    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()