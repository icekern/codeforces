# title: 2131D.py
# author: firekern
# date: 2025-08-13 21:22:41
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
    graph = defaultdict(list)
    for _ in range(n - 1):
        u, v = II()
        graph[u].append(v)
        graph[v].append(u)

    sol = 0
    leafs = 0
    fathers = []

    for i in range(1, n + 1):
        if len(graph[i]) == 1:
            leafs += 1
            continue
        sons = 0
        for j in graph[i]:
            if len(graph[j]) == 1:
                sons += 1
        if sons > 0:
            fathers.append(sons)

    if n == 2:
        PRI(0)
        return
    else:
        PRI(leafs - (max(fathers) if fathers else 0))

    

    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()