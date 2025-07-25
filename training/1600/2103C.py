# title: 2103C.py
# author: firekern
# date: 2025-07-24 18:49:03
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
    (n, k), a = II(), LI()
 
    def calc(a):
        cnt, first, total = 0, -1, 0
        for i in range(n):
            cnt += a[i] <= k
            if cnt >= i // 2 + 1:
                if first == -1:
                    first = i
                if a[i] <= k:
                    total += 1
 
        return (first, total)
 
    pref, suf = calc(a), calc(list(reversed(a)))
    print(['NO', 'YES'][(pref[0] != -1 and suf[0] != -1 and pref[0] + suf[0] + 2 < n) or (pref[1] >= 2) or (suf[1] >= 2)])

    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
