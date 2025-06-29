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
 
def solve():
    n = I()
    v = LI()
    sol = 0
    
    # v[i] + [j] > v[n - 1]
    # v[i] + [j] > v[k]
    for i in range(n):
        for j in range(i+1,n):
 
            upper_bound = bisect.bisect_left(v, v[i] + v[j])
            lower_bound = bisect.bisect_left(v, v[n - 1] - v[i] - v[j] + 1)
            
            if max(lower_bound,j + 1) < upper_bound:
                sol += upper_bound - max(lower_bound,j + 1)
 
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