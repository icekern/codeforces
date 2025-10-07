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
        pass

def solve():
    n, k = II()

    M = n * (n - 1) // 2
  
    if k < 0 or k > M:
        print(0)
        return
  
    S = M - k
    maxS = M
    maxT = n - 1
    INF = int(1e18)
  
    dp = [[INF] * (maxT + 1) for _ in range(maxS + 1)]
    prev_s = [[-1] * (maxT + 1) for _ in range(maxS + 1)]
    prev_t = [[-1] * (maxT + 1) for _ in range(maxS + 1)]
    usedL = [[-1] * (maxT + 1) for _ in range(maxS + 1)]
  
    dp[0][0] = 0
  
    for L in range(1, maxT + 1):
        T = L * (L + 1) // 2
        for s in range(maxS + 1):
            if s + T > maxS:
                break
            for t in range(maxT + 1):
                if t + L > maxT:
                    break
                    
                if dp[s][t] < INF:
                    ns, nt = s + T, t + L
                    nr = dp[s][t] + 1
                    
                    if nr < dp[ns][nt]:
                        dp[ns][nt] = nr
                        prev_s[ns][nt] = s
                        prev_t[ns][nt] = t
                        usedL[ns][nt] = L

    final_t = -1
    for t in range(maxT + 1):
        if dp[S][t] < INF and dp[S][t] <= n - t:
            final_t = t
            break
  
    if final_t == -1:
        print(0)
        return
  
    s, t = S, final_t
    Ls = []
  
    while s > 0:
        L = usedL[s][t]
        Ls.append(L)
        ps, pt = prev_s[s][t], prev_t[s][t]
        s, t = ps, pt
  
    Ls.reverse()
  
    r = len(Ls)
    sumLi = final_t
    z = maxT - sumLi
  
    a = [0] * maxT
  
    if r > 0:
        frontZeros = z - (r - 1)
        pos = 0
        
        for _ in range(frontZeros):
            pos += 1 
            
        for idx in range(r):
            for _ in range(Ls[idx]):
                a[pos] = 1
                pos += 1
            
            if idx + 1 < r:
                pos += 1 

    res = []
    st = []
  
    for i in range(n):
        st.append(i + 1)
        
        if i == n - 1 or (i < n - 1 and a[i] == 1):
            while st:
                res.append(st.pop())
  
    print(*(res))

def main():
    if MULTI:
        try:
            for _ in range(I()):
                solve()
        except:
            pass
    else:
        solve()

if __name__ == '__main__':
    main()