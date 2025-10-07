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
    n = n * 2 

    flipped_pfx_sum = [0]*(n)
    unflipped_pfx_sum = [0]*(n)
    pfx_sum = [0]*(n)

    pfx_sum[0] = a[0]
    for i in range(1,n):
        pfx_sum[i] = pfx_sum[i-1] + a[i]

    flipped_pfx_sum[0] = a[0]
    unflipped_pfx_sum[0] = 0

    for i in range(1,n):
        if i%2 == 0:
            flipped_pfx_sum[i] = flipped_pfx_sum[i-1] + a[i]
            unflipped_pfx_sum[i] = unflipped_pfx_sum[i-1]
        else:
            flipped_pfx_sum[i] = flipped_pfx_sum[i-1]
            unflipped_pfx_sum[i] = unflipped_pfx_sum[i-1] + a[i]

    solz = []

    for i in range(n//2):
        if i == 0:
            solz.append(abs(flipped_pfx_sum[n-1] - unflipped_pfx_sum[n-1]))
        else:
            pfx = pfx_sum[i - 1]
            contribute = (pfx_sum[n - 1] - pfx_sum[n - i - 1]) - pfx
            if i % 2 == 1:
                contribute += abs(unflipped_pfx_sum[n - i - 1] - unflipped_pfx_sum[i - 1] - (flipped_pfx_sum[n - i - 1] - flipped_pfx_sum[i - 1]))
            else:
                contribute += abs(flipped_pfx_sum[n - i - 1] - flipped_pfx_sum[i - 1] - (unflipped_pfx_sum[n - i - 1] - unflipped_pfx_sum[i - 1]))
            
            solz.append(abs(contribute))

    PRI(*solz)
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
