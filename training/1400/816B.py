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
    
    # n coffee
    # i th recipe is an interval [l_i, r_i]
    # given another interval [l,r] find the number of intersecting 
    
    # segment tree? 

    n, k, q = II()
    recipes = [tuple(II()) for _ in range(n)]

    range_pfx = [0] * 200002
    perfect_temp = [0] * 200002

    for l, r in recipes:
        range_pfx[l] += 1
        range_pfx[r + 1] -= 1

    for i in range(1, 200001):
        range_pfx[i] += range_pfx[i - 1]
        if range_pfx[i] >= k:
            perfect_temp[i] = 1

    for i in range(1, 200001):
        perfect_temp[i] += perfect_temp[i - 1]

    for qq in range(q):
        l, r = II()
        print(perfect_temp[r] - perfect_temp[l - 1])



def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

MULTI = False
if __name__ == '__main__':
    main()