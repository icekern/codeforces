# Created on: 12/07/2025 12:20:58
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
    n, m = II()
    
    classes = LI()
    classes.sort()

    ordered = [[] for _ in range(n + (1 if n % 2 == 1 else 0))]

    for i in range(6):
        for j in range((n + (1 if n % 2 == 1 else 0)) // 2):
            if i % 2 == 0:
                ordered[j * 2].append(classes[j])
                ordered[j * 2 + 1].append(classes[m - 1 - j])
            else:
                ordered[j * 2].append(classes[m - 1 - j])
                ordered[j * 2 + 1].append(classes[j])

    for i in range(n):
        PRI(" ".join(map(str, ordered[i])))



def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()