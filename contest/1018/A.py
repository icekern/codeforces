# title: A.py
# author: firekern
# date: 2025-08-03 22:14:03
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
    s = input().strip()
    deq = deque()

    for i in range(1, n + 1):
        deq.append(i)

    sol = []

    for i in range(n - 2, -1 , - 1):
        if s[i] == '>':
            sol.append(deq.pop())
        else:
            sol.append(deq.popleft())
    sol.append(deq.pop())
    PRI(*sol[::-1])

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
