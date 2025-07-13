# Created on: 13/07/2025 15:01:02
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
    
    s = input()
    n = len(s)

    odd = []
    even = []

    for i in range(n - 1, -1, -1):
        if int(s[i]) % 2 == 0:
            even.append(int(s[i]))
        else:
            odd.append(int(s[i]))

    to_out = []
    while len(odd) > 0 and len(even) > 0:
        if odd[-1] < even[-1]:
            to_out.append(odd.pop())
        else:
            to_out.append(even.pop())
    
    if len(odd) > 0:
        to_out.extend(reversed(odd))
    elif len(even) > 0:
        to_out.extend(reversed(even))

    PRI("".join(map(str, to_out)))

    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()