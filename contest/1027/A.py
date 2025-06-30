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
    #  4 char  express it in the form of (a + b) ^ 2

    x = I()
    sol = None

    for i in range(100):
        for j in range(100):
            if (i +j) ** 2 == x:
                sol = (i,j)
                break

    if sol is None:
        print(-1)
    else:
        print(sol[0], sol[1])
        
                

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

MULTI = True 
if __name__ == '__main__':
    main()