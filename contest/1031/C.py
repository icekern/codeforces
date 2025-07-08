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
MULTI = False

def solve():

    n,k = II()
    s = LI()

    remainder_counts = [0] * k

    for x in s:
        remainder_counts[x % k] += 1

    sol = sum(max(remainder_counts[i], remainder_counts[k - i]) for i in range(1, k // 2 + k % 2))

    if remainder_counts[0] > 0:
        sol += 1
    if k % 2 == 0:
        sol += 1 if remainder_counts[k // 2] > 0 else 0


    print(max(1,sol))

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
