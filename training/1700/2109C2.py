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
    # setup for interactive
    PRI("mul 9", flush=True)
    input().strip()

    PRI("digit", flush=True)
    input().strip()

    PRI("digit", flush=True)
    input().strip()

    PRI(f"add {n - 9}", flush=True)
    input().strip()

    PRI("!", flush=True)
    input().strip()

    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
