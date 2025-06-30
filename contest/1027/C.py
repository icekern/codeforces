import sys
from collections import defaultdict, deque
import math
import heapq

def input(): return sys.stdin.readline().rstrip('\n')
def I(): return int(input())
def II(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def SI(): return input().split()

def solve():
    n = I()
    a = LI()

    sol = 1
    last = a[0]

    for i in range(1,n):

        if last + 1 < a[i]:
            sol += 1
            last = a[i]

    print(sol)

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

MULTI = True 
if __name__ == '__main__':
    main()