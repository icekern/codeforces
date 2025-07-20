# Created on: 19/07/2025 16:32:37
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


def calculate_manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)



def solve():

    n = I()
    a = [LI() for _ in range(n)]
    s=sorted(list(range(n)),key=lambda x:a[x])
    sl=sorted([s[j] for j in range(n//2)],key=lambda x:a[x][1])
    sr=sorted([s[j] for j in range(n//2,n)],key=lambda x:-a[x][1])
    for j in range(n//2):
        print(sl[j]+1,sr[j]+1)

    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()