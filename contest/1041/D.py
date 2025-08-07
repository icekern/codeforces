# title: D.py
# author: firekern
# date: 2025-08-07 16:15:55
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
MOD = int(10**9 + 7)
factorial = [1] * (int(1e6) + 1)
for i in range(2, len(factorial)):
    factorial[i] = (factorial[i - 1] * i) % MOD

def solve():

    n,m = II()
    edges = [LI() for _ in range(m)]
    graph = defaultdict(list)
    degree = [0] * (n + 1)
    colored = [0] * (n + 1)

    sol = 0
    flag = False

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, n + 1):
        degree[i] = len(graph[i])

    queue = deque()
    queue.append(1)

    colored[1] = 1
    while queue:
        node = queue.popleft()
        degree[node] = len(graph[node])
        big_child = 0
        for neighbor in graph[node]:
            if colored[neighbor] == 0:
                colored[neighbor] = 3 - colored[node]
                queue.append(neighbor)
            else:
                if colored[neighbor] == colored[node]:
                    flag = True
            if degree[neighbor] >= 2:
                big_child += 1

        if big_child > 2:
            flag = True

    queue.append((1,0))
    depth = [0] * (n + 1)
    visited = [False] * (n + 1)

    while queue:
        node, d = queue.popleft()
        visited[node] = True
        depth[node] = d
        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append((neighbor, d + 1))
    
    s = max(depth)
    visited = [False] * (n + 1)

    for i in range(1, n + 1):
        if depth[i] == s:
            visited[i] = True

    for i in range(1, n + 1):
        if depth[i] == s - 1 and degree[i] >= 2:
            queue.append(i)
            sol = factorial[degree[i] - 1]
            sol %= MOD
            
    while queue:
        node = queue.popleft()
        visited[node] = True
        if depth[node] == 1 and degree[node] > 2:
            sol *= factorial[degree[node] - 1]
            sol %= MOD
            break
        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                sol *= factorial[degree[neighbor] - 2]
                sol %= MOD

    if flag:
        PRI(0)
    else:
        PRI(sol * 2)


def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
