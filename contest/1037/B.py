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

    n,k = II()
    a = LI()

    pfx = [0] * (n)

    pfx[0] = a[0]
    for i in range(1, n):
        pfx[i] = pfx[i-1] + a[i]

    ans = 0
    skip = k - 1
    for i in range(n):
        if i < skip:
            continue
        
        if pfx[i] - (pfx[i - k - 1] if i - k - 1 > 0 else 0) == 0:
            ans += 1
            skip = i + k

    PRI(ans)

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()