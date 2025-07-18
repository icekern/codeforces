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

    n,q = II()
    colors = LI()

    tree = [LI() for _ in range(q)]

    graph = defaultdict(defaultdict(list))

    colors = [0] * (n + 1)

    for i in range(n - 1):
        u, v, c = tree[i]
        graph[u][colors[v - 1]].append(c)
        graph[v][colors[u - 1]].append(c)

    for i in range(1, n + 1):
        for j in graph[i]:
            if colors[i - 1] != colors[j - 1]:
                PRI("YES")
                return



    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()