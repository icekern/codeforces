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
# this code is not mine is of datteiu

DEBUG = 1
MULTI = True 

def solve():
    N, M, K = map(int, input().split())
    W = int(input())
    A = list(map(int, input().split()))
 
    imos = [[0]*(M+1) for _ in range(N+1)]
    for i in range(N-K+1):
        for j in range(M-K+1):
            imos[i][j] += 1
            imos[i+K][j+K] += 1
            imos[i][j+K] -= 1
            imos[i+K][j] -= 1
    for i in range(N+1):
        for j in range(1, M+1):
            imos[i][j] += imos[i][j-1]
    for i in range(1, N+1):
        for j in range(M+1):
            imos[i][j] += imos[i-1][j]
    
    C = []
    for i in range(N):
        for j in range(M):
            C.append(imos[i][j])
    C.sort(reverse=True)
    A.sort(reverse=True)
    ans = 0
    for i in range(W):
        ans += A[i]*C[i]
    
    print(ans)

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
