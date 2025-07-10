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
    # sol <= min(a)
    # take the minimum
    # find every possible candidate 
    # min -> gcd 
    # min -> gcd
    
    n = I()
    a = LI()

    idx = 0
    min_gcd = 0
    min_steps = int(1e300)

    for i in range(n):
        min_gcd = math.gcd(min_gcd, a[i])

    queue = deque()
    visited = [False] * 5001

    for i in range(n):
        queue.append((a[i],i,0))
        visited[a[i]] = True


    while queue:
        x,i,steps = queue.popleft()

        if x == min_gcd:
            if min_steps > steps:
                min_steps = steps
                idx = i
            break

        for j in range(i + 1, n):
            new_x = math.gcd(x, a[j])
            
            if visited[new_x]:
                continue
            else:
                visited[new_x] = True
                queue.append((new_x, i, steps + 1))
    
    for i in range(n):
        if i == idx:
            continue
        if a[i] != min_gcd:
            min_steps += 1
    
    PRI(min_steps)

    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
