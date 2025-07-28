# title: A.py
# author: firekern
# date: 2025-07-27 16:37:26
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

def solve():
    n,k = II()
    a = LI()
    a.sort()
    sol = n 
    for i in range(n):
        last = 0
        flag = False
        for j in range(len(a)):
            if a[j] <= k:
                flag = True
                last = j
                

        if not flag:
            break
        
        sol -= 1
        a.remove(a[last])
        for i in range(len(a)):
            a[i] = a[i] * 2


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
