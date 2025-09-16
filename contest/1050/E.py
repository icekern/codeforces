# title: E.py
# author: firekern
# date: 2025-09-13 17:09:42
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

    n,m = II()

    a = LI()

    c_sort = [0] * (n + 1)

    for i in range(n):
        c_sort[a[i]] += 1

    for i in range(1, n + 1):
        if c_sort[i] % m != 0:
            PRI(0)
            return
        else:
            c_sort[i] //= m

    swind = [deque() for _ in range(n + 1)]


    init, sol, tot_elems = 0, 0, 0

    for i in range(n):
        tot_elems += 1
        swind[a[i]].appendleft(i)

        if len(swind[a[i]]) > c_sort[a[i]]:
            last = swind[a[i]].pop()
            tot_elems -= 1

            for j in range(init, last):
                swind[a[j]].pop()
                tot_elems -= 1
            
            init = last + 1

        sol += tot_elems

    PRI(sol)
        
def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
