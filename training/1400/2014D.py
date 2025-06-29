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

def solve():
    # 1 to n days
    # k risky jobs
    # i-th job takes place between l_i and r_i (inclusive)
    # find the max number of jobs that overlaps
    # and the min

    n, d, k = II()
    jobs = []
    for _ in range(k):
        l, r = II()
        jobs.append((l, r))
    jobs.sort()

    calendar_s = [0] * (n + 2)
    calendar_e = [0] * (n + 2)
    for i in range(k):
        calendar_s[jobs[i][0]] += 1
        calendar_e[jobs[i][1]] -= 1
    

    min_c = 1 << 30
    idx_min = 0
    max_c = 0 
    idx_max = 0
    conflicts = 0

    for i in range(1, n + 1):
        conflicts += calendar_s[i]

        if i >= d:
            
            if conflicts > max_c:
                max_c = conflicts
                idx_max = i - d + 1

            if conflicts < min_c:
                min_c = conflicts
                idx_min = i - d + 1

            conflicts += calendar_e[i - d + 1]


    print(idx_max, idx_min)


        

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

MULTI = True 
if __name__ == '__main__':
    main()