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
    n,k = II()
    a = [int(c) for c in input().strip()]

    # bob change a substring in 1s 
    # alice change a subsequence in 0s
    # who wins?

    zeros = a.count(0)
    ones = a.count(1)

    if k + zeros >= n or k > n//2:
        print("Alice")
    else:
        print("Bob")

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

MULTI = True 
if __name__ == '__main__':
    main()