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

def solve():
    # n buttons of weight w_i
    # create a colen in front of a specific button
    # move a clone to the left or right
    # press all buttons in order b1 > b2 > ... > bn
    # find the minimum number of clones that neo needs to create 

    # rittighio di code

    n = I()
    w = LI()

    paired_w = [(w[i],i) for i in range(n)]
    colored = [0] * n
    sol = 0

    paired_w.sort(key = lambda x: (-x[0], x[1]))
    segments = []
    skip = -1 
    
    for i in range(n):

        if i <= skip:
            continue

        l, r = paired_w[i][1], paired_w[i][1]
        for j in range(i + 1, n):
            if paired_w[j][0] != paired_w[i][0] or (paired_w[j][1] != l - 1 and paired_w[j][1] != r + 1):
                break
            if paired_w[j][1] == l - 1:
                l = paired_w[j][1]
            elif paired_w[j][1] == r - 1:
                r = paired_w[j][1]
            skip = j

        segments.append((paired_w[i][0],l, r))

    for i in range(len(segments)):
        w,l,r = segments[i]

        if not ((l > 0 and colored[l - 1] == 1) or (r < n - 1 and colored[r + 1] == 1)):
            sol += 1
            
        for j in range(l, r + 1):
            colored[j] = 1

    PRI(sol)


def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
