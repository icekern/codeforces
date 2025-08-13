# title: 2061B.py
# author: firekern
# date: 2025-08-12 21:30:40
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
    n = I()
    a = LI()
    a.sort()
    
    pairs = [i for i in range(n - 1) if a[i] == a[i + 1]][::-1]
    if len(pairs) >= 3:
        print(a[pairs[0]], a[pairs[0]], a[pairs[2]], a[pairs[2]])
    elif len(pairs) == 2 and pairs[1] != pairs[0] - 1:
        print(a[pairs[0]], a[pairs[0]], a[pairs[1]], a[pairs[1]])
    elif len(pairs) > 0:
        b = a[: pairs[0]] + a[pairs[0] + 2 :]
        diff = sorted([(b[i + 1] - b[i], b[i], b[i + 1]) for i in range(len(b) - 1)])
        print(
            *(
                [diff[0][1], diff[0][2], a[pairs[0]], a[pairs[0]]]
                if diff[0][0] < a[pairs[0]] * 2
                else [-1]
            ),
        )
    else:
        print(-1)


def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
