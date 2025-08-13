# title: 1997D.py
# author: firekern
# date: 2025-08-11 15:23:07
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
    s = input().strip()
    
    b = []
    cnt = 0

    for i in range(len(s)):
        if s[i] == 'A':
            cnt += 1
        else:
            b.append(cnt)
            cnt = 0

    if cnt == 0:
        PRI(sum(b))
    else:
        b.append(cnt)
        PRI(sum(b) - min(b))




def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
