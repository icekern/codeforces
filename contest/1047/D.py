# title: D.py
# author: firekern
# date: 2025-09-07 16:57:18
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
    b = LI()

    c_sort = [0] * (n + 1)
    is_valid = True

    for i in range(n):
        c_sort[b[i]] += 1

    for i in range(n + 1):
        if c_sort[i] > 0:
            if c_sort[i] % i != 0:
                is_valid = False
                break
    
    if not is_valid:
        print(-1)
        return
    else:
        bag = [[] for _ in range(n + 1)] 

        k = 0

        for i in range(1, n + 1):
            if c_sort[i] > 0:
                for j in range(c_sort[i] + 1):
                    bag[i].append(k)
                    if j % i == 0 and j != c_sort[i]:
                        k += 1
        
        res = [0] * n

        for i in range(n):
            res[i] = bag[b[i]].pop()
        
        print(*res)




def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
