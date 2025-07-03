import sys
from collections import defaultdict, deque
import math
import heapq

def input(): return sys.stdin.readline().rstrip('\n')
def I(): return int(input())
def II(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def SI(): return input().split()
PD = lambda msg: print(f"\033[92m{msg}\033[0m")

def solve():
    n,k = II()
    s = input().strip()
    a = LI()

    max_lsum = [0] * n
    max_lsum[0] = a[0] if s[0] == '1' else -int(1e18)

    for i in range(1,n):
        if s[i] == '0':
            max_lsum[i] = -int(1e18)
        else:
            max_lsum[i] = max(max_lsum[i-1] + a[i], a[i])
    
    max_rsum = [0] * n
    max_rsum[-1] = a[-1] if s[-1] == '1' else -int(1e18)

    for i in range(n-2, -1, -1):
        if s[i] == '0':
            max_rsum[i] = -int(1e18)
        else:
            max_rsum[i] = max(max_rsum[i+1] + a[i], a[i])

    for i in range(n):
        if s[i] == '0':
            a[i] = -int(1e18)

    if max(max_rsum) > k:
        print("NO")
    else:
        flag = False
        for i in range(n):
            if s[i] == '0':
                left = max_lsum[i-1] if i > 0 else 0
                right = max_rsum[i+1] if i < n-1 else 0
                a[i] = k - (left if left > 0 else 0) - (right if right > 0 else 0)
                flag = True
                break

        if not flag and max(max_lsum) != k:
            print("NO")
        else:
            print("YES")
            print(*a)

    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

MULTI = True 
if __name__ == '__main__':
    main()