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

    l, r = input().split()

    if l == r:
        print(2 * len(l))
        return

    ptr = 0
    while ptr < len(l) and l[ptr] == r[ptr]:
        ptr += 1

    if int(l[ptr]) + 1 < int(r[ptr]):
        print(2 * ptr)
    else:
        res = 2 * ptr + 1
        for i in range(ptr + 1, len(l)):
            if l[i] == '9' and r[i] == '0':
                res += 1
            else:
                break
        print(res)

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
