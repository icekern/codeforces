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

    n, k = II()
    casinos =[LI() for _ in range(n)]


    queue = deque()

    visited = [False] * n

    for i in range(n):
        if casinos[i][0] <= k <= casinos[i][1]:
            queue.append(i)
    sol = 0
    while queue:
        i = queue.popleft()
        sol = max(sol, casinos[i][2])
        if visited[i]:
            continue
        visited[i] = True

        for j in range(n):
            if not visited[j] and casinos[j][0] <= casinos[i][2] <= casinos[j][1]:
                queue.append(j)
        
    PRI(sol)

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()