# Created on: 11/07/2025 15:08:11
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

    n = I()
    a = LI()


    flag = True
    
    for i in range(1, n):
        if a[i] - a[i - 1] != a[1] - a[0]:  
            flag = False
        
    if flag:

        for i in range(n):
            if a[1] - a[0] > 0:
                a[i] = a[i] - (a[1] - a[0]) * (i + 1)
            else:
                a[i] = a[i] + (a[1] - a[0]) * (n - i)
        
    if (a[0] >= 0 and a[0] % (n + 1) == 0) and flag:
        PRI("YES")
    else:
        PRI("NO")

    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()