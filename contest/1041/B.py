# title: B.py
# author: firekern
# date: 2025-08-07 16:15:50
# github: https://github.com/icekern/codeforces

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
    s = [c for c in input().strip()]
    s = [0 if c == '.' else 1 for c in s]
    k -= 1

    if k == 0 or k == n - 1 or (s[k - 1] == 0 and s[k + 1] == 0):
        PRI(1)
        return
    else:  
        j = int(1e9)
        sol = int(1e9)
        l = 0

        for i in range(k - 1, -1, -1):
            if s[i] == 0:
                if j > k - i:
                    j = k - i
                    l = i
                    break

        for i in range(k + 1, n):
            if s[i] == 0:
                if j > i - k:
                    j = i - k
                    l = i
                    break

        if j != int(1e9):   
            s[l] = 1
        else:
            PRI(min(k + 1, n - k))
            return
    
        for i in range(k + 1, n):
            if s[i] == 0:
                sol = min(sol, i - k + 1)

        for i in range(k - 1, -1, -1):
            if s[i] == 0:
                sol = min(sol, k - i + 1)

        PRI(min(sol, k + 1, n - k))

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
