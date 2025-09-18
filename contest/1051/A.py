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
    a = LI()

    k = [(i,a[i]) for i in range(n)]
    k.sort(key=lambda x: -x[1])

    l, r = k[0][0],k[0][0]

    for i in range(1,n):
        if k[i][0] != r + 1 and  k[i][0] != l - 1 : 
            PRI('NO')
            return
        if k[i][0] == l - 1:
            l = k[i][0]
        if k[i][0] == r + 1:
            r = k[i][0]

    PRI('YES')
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
