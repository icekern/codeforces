# title: 1744E1.py
# author: firekern
# date: 2025-07-29 22:05:55
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

    a,b,c,d = II()

    for i in range(a + 1,c + 1):
        residue = math.gcd(a * b,i)
        to_find = (a * b) // residue

        if (d + 1) // to_find != b // to_find:
            for j in range(b + 1, d + 1):
                if (i * j) % (a * b) == 0:
                    PRI(i, j)
                    return
            
    PRI(-1, -1)


def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
