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
    n = I()
    s = input()

    pa = [0] * (n + 1)
    pb = [0] * (n + 1)
    for k in range(n):
        pa[k + 1] = pa[k]
        pb[k + 1] = pb[k]
        if s[k] == 'a':
            pa[k + 1] += 1
        else:
            pb[k + 1] += 1
    
    if pa[n] == pb[n]:
        print(0)
        return

    last_occurrence = {}
    min_len = n + 1 
    
    last_occurrence[0] = 0

    for j in range(n + 1):
        D = pa[n] - pb[n]
        current_diff_j = pa[j] - pb[j]
        
        target_diff_i = current_diff_j - D
        
        if target_diff_i in last_occurrence:
            i = last_occurrence[target_diff_i]
            min_len = min(min_len, j - i)
            
        last_occurrence[current_diff_j] = j
    
    if min_len > n:
        print(-1)
    else:
        if min_len == n:
            print(-1)
        else:
            print(min_len)

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()