import sys
from collections import defaultdict, deque
import math
import heapq
import bisect

MULTI = True
try:
    DEBUG = sys.stdin.isatty()
except:
    DEBUG = False

def input(): return sys.stdin.readline().rstrip('\n')
def I(): return int(input())
def II(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def SI(): return input().split()
def PRI(*args, **kwargs):
    if DEBUG:
        print(f"\033[92m{kwargs.get('sep', ' ').join(map(str, args))}\033[0m", file=sys.stderr, **kwargs)
    else:
        print(*args, **kwargs)

def solve():
    n, m = II()
    s = input()
    v = LI()

    ans = set(v)
    
    pos = 1

    for c in s:
        if c == 'A':
            pos += 1
            ans.add(pos)
        else:
            pos += 1
            while pos in ans:
                pos += 1
            ans.add(pos)
            pos += 1
            while pos in ans:
                pos += 1
    
    PRI(len(ans))
    PRI(*sorted(list(ans)))

def main():
    if MULTI:
        try:
            for _ in range(I()):
                solve()
        except (IOError, ValueError):
            pass
    else:
        solve()

if __name__ == '__main__':
    main()