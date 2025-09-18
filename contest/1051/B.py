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
    
    n,k = II()
    a = LI()
    b = LI()

    a.sort(reverse=True)
    b.sort()

    i = 0
    j = 0
    sol = sum(a)
    while i < n and j < k and i + b[j] - 1 < n:
        sol -= a[i + b[j] - 1]
        i += b[j]
        j += 1
    
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
