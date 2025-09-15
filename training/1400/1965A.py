# Created on: 2025-08-09 20:05

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

# https://github.com/icekern/codeforces

DEBUG = 1
MULTI = True

def solve():
    n = I()
    a = set(LI())
    a = list(a)
    a.sort()

    if a[0] != 1:
        print("Alice")
    else:      
        control = 1
        for i in range(1, len(a)):
            if a[i - 1] == i:
                control = 1 - control
            else:
                break
        
        if control == 0:
            print("Bob")
        else:
            print("Alice")

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()