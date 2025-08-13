# title: E.py
# author: firekern
# date: 2025-08-10 16:32:54
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
    a,b = LI(), LI()
    c = [i for i in a]
    flag = True

    if a[n - 1] != b[n - 1]:
        print("NO")
        return

    for i in range(n - 2, -1 , -1):
        if a[i] == b[i]:
            continue
        else:
            if a[i] ^ c[i + 1] == b[i]:
                a[i] = a[i] ^ c[i + 1]
            elif a[i] ^ a[i + 1] == b[i]:
                a[i] = a[i] ^ a[i + 1]
            
            if a[i] != b[i]:
                flag = False
                break
    

    if flag:
        print("YES")
    else:
        print("NO")

    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
