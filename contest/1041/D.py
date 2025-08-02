# title: D.py
# author: firekern
# date: 2025-08-02 12:55:19
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
    n=int(input())
    arr=list(map(int,input().split()))
    cur=0
    for i in range(n):
        for j in range(i):
            if arr[i]<arr[j]:
                cur+=1
 
    for i in range(n):
        x=0
        for j in range(n):
            if arr[j]>arr[i]:
                if j<i:
                    x+=1
                else:
                    x-=1
        cur-=max(x,0)
    PRI(cur)

    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
