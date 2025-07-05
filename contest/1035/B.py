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

DEBUG = 0
MULTI = True 

def euclidean_distance(x1, y1, x2, y2):
    return int(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))

def solve():
    n = I()
    px, py, qx, qy = II()
    distances = LI()

    d_target = math.sqrt((px - qx)**2 + (py - qy)**2)

    if n == 0:
        return d_target == 0.0

    sum_distances = sum(distances)
    max_distance = sum_distances

    a_max = 0.0
    if distances: 
        a_max = max(distances)

    min_distance = max(0.0, 2 * a_max - sum_distances)

    epsilon = 1e-9
    if min_distance - epsilon <= d_target <= max_distance + epsilon:
        print("YES")
    else:
        print("NO")

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
