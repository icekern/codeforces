# Current Date & Time: 21 CURRENT_TIME
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
    n = I()
    a = LI()
    s = input().strip()

    q1,q2 = [],[]

    pfx = [0] * n
    pfx[0] = a[0]
    for i in range(1,n):
        pfx[i] += a[i] + pfx[i - 1]

    for i in range(n):
        if s[i] == "L":
            q1.append(a[i])

    for i in range(n - 1, -1, -1):
        if s[i] == "R":
            q2.append(a[i])

    q1 = q1[::-1]
    q2 = q2[::-1]
    while q1 and q2:
        i,j = q1.pop(),q2.pop()
        sol += pfx[j] - (pfx[i - 1] if i > 0 else 0)

    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
