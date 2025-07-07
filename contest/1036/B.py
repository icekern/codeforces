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

    # array a of lenght n 
    #

    n = I()
    a = LI()

    min_prefix = [0] * n
    for i in range(n):
        if i == 0:
            min_prefix[i] = a[i]
        else:
            min_prefix[i] = min(min_prefix[i - 1], a[i])
    

    p_sum = min_prefix[0]
    sol = a[0] + a[1]
    flag = False
    for i in range(1, n):

        if min_prefix[i] == min_prefix[i - 1]:
            flag = True

        if i + 1 < n:
            if flag:
                sol = min(sol, p_sum + min_prefix[i])
            else:
                sol = min(sol, p_sum + min(min_prefix[i] + a[i + 1], min_prefix[i - 1]))

        p_sum += min_prefix[i]
            
        sol = min(sol, p_sum + a[i])

        
    sol = min(sol, p_sum)

    PRI(sol)


    # set a[i] = a[i] + a[j]
    # set a[j] = 0

    # this operation is used every time on the second element




    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()

