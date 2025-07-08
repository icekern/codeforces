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

    w,h,a,b = II()
    x1, y1, x2, y2 = II()

    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    diffy = abs(y1 + b - y2)
    diffx = abs(x1 + a - x2)

    PRI(f"diffx: {diffx}, diffy: {diffy}, a: {a}, b: {b}")

    PRI(f"x1: {x1}, y1: {y1}, x2: {x2}, y2: {y2}, y1 + b: {y1 + b}")
    if diffx < a and  y1 < y2 < y1 + b:
        PRI("NO")
    else:
        PRI("YES")









    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
