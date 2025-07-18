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

# https://github.com/icekern/codeforces

DEBUG = 1
MULTI = True 

def solve():

    n = I()
    a = LI()
    b = LI()

    c = [math.lcm(x, y) for x, y in zip(a, b)]

    p_gcd = [0] * n
    p_gcd[0] = c[0]
    s_gcd = [0] * n
    s_gcd[-1] = c[-1]

    for i in range(1, n):
        p_gcd[i] = math.gcd(p_gcd[i - 1], c[i])

    for i in range(n - 2, -1, -1):
        s_gcd[i] = math.gcd(s_gcd[i + 1], c[i])

    flag = True
    for i in range(n):
        if p_gcd[i] != a[i] or s_gcd[i] != b[i]:
            flag = False
            break

    if flag:
        PRI("YES")
    else:
        PRI("NO")
    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()