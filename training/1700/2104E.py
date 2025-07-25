# title: 2104E.py
# author: firekern
# date: 2025-07-24 17:26:31
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

DEBUG = 0
MULTI = False

def solve():

    n,k = II()
    s = input().strip()
    q = I()
    pfx = [[0 for _ in range(k)] for _ in range(n)]
    fast_cf = defaultdict(list)

    for i in range(n):
        fast_cf[ord(s[i]) - ord('a')].append(i)
        pfx[i][ord(s[i]) - ord('a')] += 1

        if i > 0:
            for j in range(k):
                pfx[i][j] += pfx[i - 1][j]

    while q > 0:
        q -= 1

        t = input().strip()
        m = len(t)

        idx = 0
        r = -1
        
        flag = True
        while idx < m:
            r = bisect.bisect_right(fast_cf[ord(t[idx]) - ord('a')], r)
            if r == len(fast_cf[ord(t[idx]) - ord('a')]):
                flag = False
                break
            else:
                r = fast_cf[ord(t[idx]) - ord('a')][r]
            idx += 1


        if flag:
            PRI(min([pfx[n - 1][i] - pfx[r][i] for i in range(k)]) + 1)
        else:
            PRI(0)

    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
