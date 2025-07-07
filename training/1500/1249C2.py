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

DEBUG = 0
MULTI = True 

def solve():
    n = I()
    m = n
    power = int(math.log(n, 3)) + 1
    not_taken = []
    sol = 0
    while n > 0 and power >= 0:
        if n >= 3 ** power:
            n -= 3 ** power
            sol += 3 ** power
            power -= 1
        else:
            not_taken.append(3 ** power)
            power -= 1

    r_sol = sol

    if sol < m:
        diff = int(1e20)

        print(f"sol: {sol}, not_taken: {not_taken}, m: {m}")
        for i in range(len(not_taken)):
            if not_taken[i] >= m:
                diff = not_taken[i] - m
                r_sol = not_taken[i]

            if sol + not_taken[i] - m <= diff and sol + not_taken[i] - m >= 0:
                diff = sol + not_taken[i] - m
                r_sol = sol + not_taken[i]
            
    PRI(r_sol)

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
