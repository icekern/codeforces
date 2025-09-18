import sys
from collections import defaultdict, deque
import math
import heapq
import bisect

MULTI = True
try:
    DEBUG = sys.stdin.isatty()
except:
    DEBUG = False

# --- Input Helpers ---
def input(): return sys.stdin.readline().rstrip('\n')
def I(): return int(input())
def II(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def SI(): return input().split()
def PRI(*args, **kwargs):
    if DEBUG:
        print(f"\033[92m{kwargs.get('sep', ' ').join(map(str, args))}\033[0m", file=sys.stderr, **kwargs)
    else:
        print(*args, **kwargs)

# --- solve ---
def solve():
    n = I()

    graph = defaultdict(list)

    for i in range(n - 1):
        u,v,x,y = II()
        graph[u].append((v,(x,y)))
        graph[v].append((u,(y,x)))


    vis = [False] * (n + 1)
    deq = deque()

    sol = 0
    deq.append(1)
    # root at 0,0
    l, r = 1, n
    perm = [0] * (n + 1)
    sol = 0

    while deq:
        node = deq.pop()
        vis[node] = True

        dx_sum, dy_sum = 0, 0

        for x, (dx, dy) in graph[node]:
            if not vis[x]:
                deq.append(x)
                dx_sum += dx
                dy_sum += dy


        PRI(dx_sum, dy_sum)
        if dx_sum > dy_sum:
            perm[node] = r
            r -= 1
            sol += dx_sum
        else:
            perm[node] = l
            l += 1
            sol += dy_sum

    PRI(sol)
    PRI(*perm[1:])

# --- main ---
def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
