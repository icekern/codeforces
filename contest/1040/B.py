# title: B.py
# author: firekern
# date: 2025-07-27 16:43:51
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
    n = I()
    a = LI()

    k = deque(a)
    flip = False

    solve = ""
    for i in range(0,n,2):
        if len(k) == 1:
            solve += "L"
            break
        if len(k) == 0:
            break

        if not flip:
            if k[0] < k[-1]:
                solve += "LR"
            else:
                solve += "RL"
            k.popleft()
            k.pop()
            flip = True
        else:
            if k[0] > k[-1]:
                solve += "LR"
            else:
                solve += "RL"
            k.pop()
            k.popleft()
            flip = False
    
    PRI(solve)


    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
