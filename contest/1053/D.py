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

# --- Global Precomputation ---
MOD = 998244353
MAX_F = 400005

fact = [1] * MAX_F
ifact = [1] * MAX_F

def precomp():
    for i in range(1, MAX_F):
        fact[i] = (fact[i-1] * i) % MOD
    
    ifact[MAX_F-1] = pow(fact[MAX_F-1], MOD - 2, MOD)
    for i in range(MAX_F - 2, -1, -1):
        ifact[i] = (ifact[i+1] * (i+1)) % MOD

precomp()

def C(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * ifact[r] % MOD * ifact[n-r] % MOD

# --- solve ---
def solve():
    n = I()
    a = LI()

    if sum(a) != n:
        PRI(0)
        return

    m = (n + 1) // 2
    
    for i in range(m, n):
        if a[i] != 0:
            PRI(0)
            return
            
    ans = 1
    u = 0
    
    for r in range(m, 0, -1):
        sr = n + 2 - 2*r
        av = sr - u
        c = a[r-1]
        
        if c < 0 or c > av:
            PRI(0)
            return
        
        ans = (ans * C(av, c)) % MOD
        u += c
        
    PRI(ans)

# --- main ---
def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()