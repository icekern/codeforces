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
    n,m = II()
    sol = 0
    matrix = [LI() for _ in range(n)]
    c_sort = [[] for i in range(101)]

    for i in range(n):
        for j in range(m):
            c_sort[matrix[i][j]].append((i, j))

    for i in range(100, -1, -1):

        if c_sort[i] == []:
            continue
        
        x_count = defaultdict(int)
        y_count = defaultdict(int)
        
        for p in c_sort[i]:
            x_count[p[0]] += 1
            y_count[p[1]] += 1

        x_max = max(x_count, key=x_count.get)
        y_max = max(y_count, key=y_count.get)
        flag = False

        total = len(c_sort[i])
        collinear = 0

        
        if total <= 2:
            flag = True


        for p in c_sort[i]:
            if (p[0] == x_max and p[1] == y_max) and x_count[x_max] >= 2 and y_count[y_max] >= 2:
                collinear += 1
                
        if (0 if x_count[x_max] == 1 else x_count[x_max]) + \
        (0 if y_count[y_max] == 1 else y_count[y_max]) - \
        collinear == total or y_count[y_max] == total - 1 or x_count[x_max] == total - 1:
            flag = True
        
        if flag:
            sol = i - 1
        else:
            sol = i

        break
    
    PRI(sol)
        
def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
