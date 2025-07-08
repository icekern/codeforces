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

    n,m,k = II()
    k -= 1
    matrix = [[c for c in input().strip()] for _ in range(n)]
    pfx_2d = [[0] * (m + 1) for _ in range(n + 1)]
    sol = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            pfx_2d[i][j] = pfx_2d[i - 1][j] + pfx_2d[i][j - 1]  - pfx_2d[i - 1][j - 1]+ (1 if matrix[i - 1][j - 1] == "g" else 0)
        
    # the rectangle can exceed the bounds of the matrix
    def calculate_rectangle_sum(x1, y1, x2, y2):
        x1 = max(1, x1)
        y1 = max(1, y1)
        x2 = min(n, x2)
        y2 = min(m, y2)
        return pfx_2d[x2][y2] - pfx_2d[x1 - 1][y2] - pfx_2d[x2][y1 - 1] + pfx_2d[x1 - 1][y1 - 1]
    
    total_gold = sum(i.count("g") for i in matrix)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if matrix[i - 1][j - 1] == ".":
                gold_inside_crop = calculate_rectangle_sum(i - k, j - k, i + k, j + k)
                sol = max(sol, total_gold - gold_inside_crop)

    PRI(sol)

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
