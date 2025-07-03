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
    
    n = I()
    a = LI()

    graph = defaultdict(list)

    for i in range(n - 1):
        u,v = LI()
        graph[u].append(v)
        graph[v].append(u)
    dp = [[0,0] for _ in range(n + 1)]
    

    stack = [1]
    visited = [False] * (n + 1)
    visited[1] = True
    while stack:
        
        node = stack.pop()

        daddy = dp[node][1]
        granny = dp[daddy][1]

        dp[node][0] = a[node - 1] + max(0,dp[granny][0] - a[daddy - 1])

        for neighbor in graph[node]:
            if not visited[neighbor]:
                dp[neighbor][1] = node
                visited[neighbor] = True
                stack.append(neighbor)
    
    print(*[i[0] for i in dp[1:]])


def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

MULTI = True 
if __name__ == '__main__':
    main()