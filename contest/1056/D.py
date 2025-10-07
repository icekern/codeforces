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
    
    max_inversions = n * (n - 1) // 2
    
    if k < 0 or k > max_inversions:
        print(0)
        return
        
    target_sum = max_inversions - k
    max_s = max_inversions
    max_t = n - 1
    INF = 10**9
    
    dp = [[INF] * (max_t + 1) for _ in range(max_s + 1)]
    prev_s_val = [[-1] * (max_t + 1) for _ in range(max_s + 1)]
    prev_t_val = [[-1] * (max_t + 1) for _ in range(max_s + 1)]
    used_len = [[-1] * (max_t + 1) for _ in range(max_s + 1)]
    
    dp[0][0] = 0
    
    for L in range(1, max_t + 1):
        sum_inversions = L * (L - 1) // 2
        
        for s in range(max_s + 1):
            for t in range(max_t + 1):
                if dp[s][t] < INF:
                    ns = s + sum_inversions
                    nt = t + L

                    if ns <= max_s and nt <= max_t:
                        nr = dp[s][t] + 1
                        
                        if nr < dp[ns][nt]:
                            dp[ns][nt] = nr
                            prev_s_val[ns][nt] = s
                            prev_t_val[ns][nt] = t
                            used_len[ns][nt] = L

    final_t = -1
    for t in range(max_t + 1):
        if dp[target_sum][t] < INF and dp[target_sum][t] <= n - t: 
            final_t = t
            break
    
    if final_t == -1:
        print(0)
        return
        
    s = target_sum
    t = final_t
    block_lengths = []
    
    while s > 0:
        L = used_len[s][t]
        block_lengths.append(L)
        ps = prev_s_val[s][t]
        pt = prev_t_val[s][t]
        s = ps
        t = pt
    
    block_lengths.reverse()
    
    r = len(block_lengths)
    sum_t = final_t
    z = max_t - sum_t
    
    arr_structure = [0] * max_t
    
    if r > 0:
        num_leading_zeros = z - (r - 1)
        pos = 0
        
        for _ in range(num_leading_zeros):
            arr_structure[pos] = 0
            pos += 1
            
        for idx in range(r):
            for _ in range(block_lengths[idx]):
                arr_structure[pos] = 1
                pos += 1
            if idx + 1 < r:
                arr_structure[pos] = 0
                pos += 1
                
    result_perm = []
    stack = []
    
    for i in range(n):
        stack.append(i + 1)
        
        is_last = (i == n - 1)
        is_block_end = (i < n - 1 and arr_structure[i] == 1)
        
        if is_last or is_block_end:
            while stack:
                result_perm.append(stack.pop())
    
    print(*(result_perm))

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()