import sys
from collections import defaultdict, deque
import math
import heapq

def input(): return sys.stdin.readline().rstrip('\n')
def I(): return int(input())
def II(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def SI(): return input().split()

def solve():
    # i need to do a prefix sum on the graph
    # to redo tomorrow i fucked up the reading
    
    n = I()
    a = LI()

    # dfs flip 2 sums that alternates
    graph = defaultdict(list)

    for i in range(n - 1):
        u,v = LI()
        graph[u].append(v)
        graph[v].append(u)

    # we need to do a dfs on the graph and flip the values
    # iterative

    stack = [(1,0)]
    visited = [False] * (n + 1)
    visited[1] = True

    pfx_sum = [0,0]
    flip = 0

    solutions = []

    while stack:
        node,phase = stack.pop()

        if phase == 0:
            if flip == 0:
                flip = 1
                pfx_sum[0] += a[node - 1]
                solutions.append((node,pfx_sum[0] - pfx_sum[1]))
            else:
                flip = 0
                pfx_sum[1] += a[node - 1]
                solutions.append((node,pfx_sum[1] - pfx_sum[0]))

            stack.append((node, 1))
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append((neighbor,0))
        else:
            if flip == 0:
                pfx_sum[0] -= a[node - 1]
            else:
                pfx_sum[1] -= a[node - 1]

    solutions.sort(key=lambda x: x[0])

    print(' '.join(str(x[1]) for x in solutions))

    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

MULTI = True 
if __name__ == '__main__':
    main()