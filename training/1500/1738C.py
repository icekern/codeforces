# title: 1738C.py
# author: firekern
# date: 2025-07-29 21:27:13
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

    odd, even = 0,0 

    for i in range(n):
        if a[i] % 2 == 0:
            even += 1
        else:
            odd += 1

    if  odd % 4 == 2:
        PRI("Bob")
    elif odd % 4 == 3:
        PRI("Alice")
    elif odd % 4 == 0:
        PRI("Alice")
    elif even % 2 == 1:
        PRI("Alice")
    else:
        PRI("Bob")


def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
