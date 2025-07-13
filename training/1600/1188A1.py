# Created on: 13/07/2025 14:29:17
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
MULTI = False 

def solve():

    graph = defaultdict(list)
    n = I()

    for _ in range(n - 1):
        u, v = II()
        graph[u].append(v)
        graph[v].append(u)
    
    if n == 2:
        PRI("YES")
    else:
        root = 0

        for i in range(1, n + 1):
            if len(graph[i]) > 1:
                root = i
                break


        stack = deque()
        visited = [False] * (n + 1)
        stack.append((root, 0))
        color = [0] * (n + 1)
        color[0] = 1

        # DFS
        while stack:
            node, phase = stack.pop()

            visited[node] = True

            color[node] = len(graph[node])

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    stack.append((neighbor, 0))

        PRI("YES" if 2 not in color else "NO")





    


    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()