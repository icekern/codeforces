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

def calculate_mex(a):

    mex = 0
    for num in a:
        if num == mex:
            mex += 1
        elif num > mex:
            break
    return mex

def solve():

    n = I()
    a = LI()
    a.sort()

    mex = calculate_mex(a) - 1
    c_sort = [0] * (mex + 1)
    k_solutions = [0] * (n + 2)

    for i in range(n):
        if a[i] <= mex:
            c_sort[a[i]] += 1
        
    scarto = n

    for i in range(mex + 1):
        scarto -= c_sort[i]
        k_solutions[c_sort[i]] += 1
        k_solutions[min(c_sort[i] + scarto,n + 1)] -= 1
        scarto += c_sort[i] - 1

    for i in range(1, n + 2):
        k_solutions[i] += k_solutions[i - 1]

    for i in range(0, n + 2):
        k_solutions[i] += 1

    print(" ".join(map(str, k_solutions[:n + 1])))

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

MULTI = True 
if __name__ == '__main__':
    main()