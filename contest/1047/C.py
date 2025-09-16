# title: C.py
# author: firekern
# date: 2025-09-07 16:43:32
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

    a,b = II()


    # a + b % 2 == 0
    # togliere i divisori dispari dispari 
    # pari pari 
    # 1 ci devono essere 2 
    # 2 ci devono essere 2 
    # ho dei 2 in b 
    # 


    two_in_b = 0

    temp = b
    while temp % 2 == 0:
        two_in_b += 1
        temp //= 2

    if b % 2 == 0:
        a *= 2 ** (two_in_b - 1)
        b //= 2 ** (two_in_b - 1)
        a *= b // 2
        b = 2

        if a % 2 == 0:
            PRI(a + b)
        else:
            PRI(-1)
    else:
        if a % 2 == 0:
            PRI(-1)
        else:
            PRI(a * b + 1)


def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
