# title: 2093D.py
# author: firekern
# date: 2025-07-25 20:56:03
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

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [1] * (n + 1)

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def solve():
    n, m1, m2 = II()
    dsu1 = DSU(n)
    dsu2 = DSU(n)
    to_remove = 0
    to_add = 0
    edges1 = []
    edges2 = []

    for _ in range(m1):
        u, v = II()
        edges1.append((u, v))
        dsu1.union(u, v)

    for _ in range(m2):
        u, v = II()
        edges2.append((u, v))
        dsu2.union(u, v)
    
    edges1_true = []

    for edge in edges1:
        u, v = edge
        if dsu2.find(u) != dsu2.find(v) and dsu1.find(u) == dsu1.find(v):
            to_remove += 1
        else:
            edges1_true.append(edge)

    dsu1 = DSU(n)

    for edge in edges1_true:
        u, v = edge
        dsu1.union(u, v)

    for edge in edges2:
        u, v = edge
        if dsu2.find(u) == dsu2.find(v) and dsu1.find(u) != dsu1.find(v):
            to_add += 1
            dsu1.union(u, v)

    PRI(to_remove + to_add)

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
