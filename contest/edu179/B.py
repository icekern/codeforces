# Created on: 12/07/2025 11:59:12
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
    dimensions = [LI() for _ in range(m)]


    fibo  = [0] * n
    fibo[0] = 1
    fibo[1] = 2
    for i in range(2, n):
        fibo[i] = fibo[i-1] + fibo[i-2]
    
    sols = ""
    for i in range(m):

        x,y,z = dimensions[i]

        if x >= fibo[n-1] and y >= fibo[n - 1] and z >= fibo[n - 1] + fibo[n - 2] or \
           x >= fibo[n-1] and z >= fibo[n - 1] and y >= fibo[n - 1] + fibo[n - 2] or \
           y >= fibo[n-1] and z >= fibo[n - 1] and x >= fibo[n - 1] + fibo[n - 2]:
            sols += "1"
        else:
            sols += "0"
    PRI(sols)
    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()