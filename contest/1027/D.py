import sys
from collections import defaultdict, deque
import math
import heapq

def input(): return sys.stdin.readline().rstrip('\n')
def I(): return int(input())
def II(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def SI(): return input().split()


def solve():
    # u can move the a moster in whatever direction you want
    # minimize the number of coins 
    # it s calculated as the area of the rectagles that you use to kill the monsters

    # X
    #               
    #          X
    #               X
    #          X
    #               X

    # only one rectangle is needed to kill all the monsters
    # is it possible to bruteforce the solution?

    # at the end what we need is to find the 4 corners that will cover everything
    # at most we have 4 corners 

    # we start from the left and we find the first with a sort 
    # so we can sort to find the 4 corners

    n = I()

    points = [tuple(II()) for _ in range(n) ]

    points.sort()

    top_right = points[-1]
    bottom_right = points[0]

    points.sort(key=lambda x: x[1])

    top_left = points[-1]
    bottom_left = points[0]

    # now we have the 4 corners what we can do is calculate the area as
    # max(x...) - min(x...) + 1 * max(y...) - min(y...) + 1
    # we don t care if we put a monster and we have space 
    # but if we don't? we can t put that monster in the rectangle

    pivot = set([top_left, top_right, bottom_left, bottom_right])
    pivot = list(pivot)

    x1 = min(p[0] for p in points)
    x2 = max(p[0] for p in points)
    y1 = min(p[1] for p in points)
    y2 = max(p[1] for p in points)

    sol = (x2 - x1 + 1) * (y2 - y1 + 1)

    if n != 1:
        for p in pivot:

            x1,x2,y1,y2 = int(1e9),0,int(1e9),0

            for j in points:
                if j == p:
                    continue
                x1 = min(x1, j[0])
                x2 = max(x2, j[0])
                y1 = min(y1, j[1])
                y2 = max(y2, j[1])

            
            area = (x2 - x1 + 1) * (y2 - y1 + 1)

            
            if area == n - 1:
                sol = min(sol, min((x2 - x1 + 2) * (y2 - y1 + 1),(x2 - x1 + 1) * (y2 - y1 + 2)))
            else:
                sol = min(sol, area)
            
    print(sol)

    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

MULTI = True 
if __name__ == '__main__':
    main()