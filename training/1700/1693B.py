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

    graph = defaultdict(list)

    n = I()
    edg = LI()


    for i in range(1, n):
        graph[edg[i - 1]].append(i + 1)

    lr = [LI() for _ in range(n)]

    l = [x[0] for x in lr]
    r = [x[1] for x in lr]

    deq = deque()

    deq.append((1,l[0]))

    sol = 0
    while deq:
        node, w = deq.pop()

        for x in graph[node]:
            if l[x - 1] <= w <= r[x - 1]:
                w = min(w,r[x - 1])
            else:
                w = l[x - 1]
                sol += 1
            
            deq.append((x,w))

    PRI(sol)    
            
    


    pass

# --- main ---
def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
