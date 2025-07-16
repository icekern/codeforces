# Created on: 16/07/2025 13:09:09
# Author: Porcelli
# GitHub: https://github.com/icekern/codeforces

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


    n = I()
    s = input().strip()
    res = len(s)

    if n % 2 == 0:
        v = [[0] * 26 for _ in range(2)]
        for i in range(n):
            v[i % 2][ord(s[i]) - ord('a')] += 1
        for i in range(2):
            mx = max(v[i])
            res -= mx
        print(res)
    else:
        pref = [[0] * 26 for _ in range(2)]
        suf = [[0] * 26 for _ in range(2)]
        for i in range(n - 1, -1, -1):
            suf[i % 2][ord(s[i]) - ord('a')] += 1
        for i in range(n):
            suf[i % 2][ord(s[i]) - ord('a')] -= 1
            ans = n
            for k in range(2):
                mx = 0
                for j in range(26):
                    mx = max(mx, suf[1 - k][j] + pref[k][j])
                ans -= mx
            res = min(res, ans)
            pref[i % 2][ord(s[i]) - ord('a')] += 1
        print(res)

    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()