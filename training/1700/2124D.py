# title: 2124D.py
# author: firekern
# date: 2025-07-23 18:46:08
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
    b = a.copy()
    b.sort(reverse=True)
    c = []

    ele = b[n - k + 1] if n - k + 1 != n else -1

    for i in range(n):
        if a[i] <= ele:
            c.append(a[i])

    sol = 0
    for i in range(n - k, -1, -1):
        if ele == b[i]:
            sol += 1

    flag = True
    s = len(c) - i - 1
    e = 0
    while e <= s:
        if c[e] != c[s]:
            if sol > 0 and (c[e] == ele or c[s] == ele):
                if c[s] == ele:
                    sol -= 1
                    s -= 1
                else:
                    sol -= 1
                    e += 1
            else:
                flag = False
                break
        else:
            e += 1
            s -= 1
    
    if flag:
        PRI("YES")
    else:
        PRI("NO")

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
