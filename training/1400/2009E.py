# Created on: 15/07/2025 15:24:27
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
    def val(mid):
        val1 = (mid+k-1+k)*mid//2
        val2 = (k+n-1+k)*n//2 - val1
        return val1,val2
    
    n,k = map(int,input().split())
    lo = 1
    hi = n
    curr = 1
    while lo <= hi:
        mid = (lo+hi)//2
        a,b = val(mid)
        if b>a:
            curr = mid
            lo = mid+1
        else:
            hi = mid-1
    a1,b1 = val(curr)
    a2,b2 = val(curr+1)
    print(min(b1-a1,a2-b2))    


def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()