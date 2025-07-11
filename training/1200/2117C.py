# Created on: 11/07/2025 14:47:08
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

    s1 = set()
    s1.add(str(a[0]))
    s2 = set()
    sol = 1

    for i in range(1,n):
        s2.add(str(a[i]))
        if str(a[i]) in s1:
            s1.remove(str(a[i]))
        
        if len(s1) == 0:
            sol += 1
            s1, s2 = s2, s1
        
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