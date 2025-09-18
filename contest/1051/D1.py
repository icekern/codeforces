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

# --- Input Helpers ---
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

# --- solve ---
def solve():
    n = I()
    MOD = int(10**9 + 7)

    a = LI()

    dp = [[[0 for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(n)]

    dp[0][a[0]][0] = 1
    dp[0][0][a[0]] = 1

    for i in range(1,n):

        dp[i][a[i]][0] += 1
        dp[i][0][a[i]] += 1

        for j in range(a[i] + 1):
            for k in range(n + 1):
                dp[i][a[i]][k] += dp[i - 1][j][k]
                dp[i][a[i]][k] %= MOD

        for k in range(a[i] + 1):
            for j in range(n + 1):
                dp[i][j][a[i]] += dp[i - 1][j][k]
                dp[i][j][a[i]] %= MOD

        for j in range(n + 1):
            for k in range(n + 1):
                dp[i][j][k] += dp[i - 1][j][k]
                dp[i][j][k] %= MOD
        
    sol = 0
    for i in range(n + 1):
        for j in range(n + 1):
            sol += dp[n - 1][i][j]
            sol %= MOD

    PRI(sol + 1)

# --- main ---
def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
