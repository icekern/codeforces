# Created on: 20/07/2025 14:31:32
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
    n,m = II()
    a = LI()
    start = max(a)
    lb = 0
    rb = k 
    for i in a:
        d = (start-i)%(2*k)
        if d < k:
            rb = min(k-d-1,rb)
        else:
            lb = max(2*k-d,lb)
    if lb <= rb:
        print (start+lb)
    else:
        print (-1)


    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()