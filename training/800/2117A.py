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

    n,k = II()
    a = LI()

    first_0 = 0
    last_0 = 0

    for i in range(n):
        if a[i] == 1:
            first_0 = i
            break
    for i in range(n - 1, -1, -1):
        if a[i] == 1:
            last_0 = i
            break
    

    if abs(last_0 - first_0 + 1) <= k:
        PRI("YES")
        return
    else:
        PRI("NO")



def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
