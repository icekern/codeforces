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

    # you have an array a 
    # 2 operations

    # chose a prefix substitute it with the min(prefix)
    # chose a suffix substitute it with the min(suffix)

    # determine whether the i th element can be obtain alone

    #

    n = I()
    a = LI()


    min_prefix = [int(1e7)] * n
    max_suffix = [0] * n

    for i in range(n):
        if i == 0:
            min_prefix[i] = a[i]
        else:
            min_prefix[i] = min(min_prefix[i - 1], a[i])
    
    for i in range(n - 1, -1, -1):
        if i == n - 1:
            max_suffix[i] = a[i]
        else:
            max_suffix[i] = max(max_suffix[i + 1], a[i])

    remains = [0] * n
    remains[0] = 1
    remains[n - 1] = 1

    for i in range(1,n-1):
        if (min_prefix[i] >= a[i] and max_suffix[i] >= a[i]) or (min_prefix[i] <= a[i] and max_suffix[i] <= a[i]):
            remains[i] = 1

    print("".join(map(str, remains)))



def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

MULTI = True 
if __name__ == '__main__':
    main()