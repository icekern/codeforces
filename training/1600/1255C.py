# Created on: 13/07/2025 15:56:01
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
MULTI = False

def solve():

    n = I() - 2
    triplets = [tuple(II()) for _ in range(n)]
    original_array = [0] * (n + 2)

    c_sort = [[] for _ in range(n + 3)]


    for i in range(n):
        for j in range(3):
            c_sort[triplets[i][j]].append(i)

    start = 0
    for i in range(1, n + 3):
        if len(c_sort[i]) == 1:
            original_array[0] = i
            start = i
            break
    
    for i in range(1, n + 3):
        if len(c_sort[i]) == 2 and (start in triplets[c_sort[i][0]] or start in triplets[c_sort[i][1]]):
            original_array[1] = i
            start = i
            break
            

    taken = set(original_array[:2])
    

    for i in range(2, n + 3):
        for k in [triplets[c_sort[start][_]] for _ in range(len(c_sort[start]))]:
            flag = True
            for r in range(3):
                if (k[r] not in taken) and (k[(r + 1)%3] in taken) and (k[(r - 1)% 3] in taken):
                    original_array[i] = k[r]
                    start = k[r]
                    taken.add(k[r])
                    flag = False
                    break
            if not flag:
                break

    
    PRI(*original_array)
    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()