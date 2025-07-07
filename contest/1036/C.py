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
    # array b of lenght n 
    # b = a sse b[i + 1] // b[i] == 0 sol = n sol --
    # if not  take all b[i + 1]//b[i]  find the GCD of all of them 
    # if b[i + 1] // b[i]

    # build a matrix of n x rad(n) x log(n)

    n = I()
    a = LI()

    gcd_array = [1] * n

    for i in range(n - 1, -1, - 1):
        if i == n - 1:
            gcd_array[i] = a[i]
        else:
            gcd_array[i] = int(math.gcd(gcd_array[i + 1], a[i]))
    x = 1
    for i in range(n - 1):
        x = math.lcm(x, a[i] // gcd_array[i]) 
        

    PRI(x)

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
