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

def solve():
    n,k = II()
    a = LI()
    beauty = 0

    for i in range(0, 60):
        for j in range(len(a)):
            if a[j] & (1 << i) == 0 and k >= (1 << i):
                k -= (1 << i)
                a[j] ^= (1 << i)
    
    for x in a:
        temp = x
        while temp > 0:
            if temp & 1:
                beauty += 1
            temp >>= 1

    PRI(beauty)

    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
