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
    n,l,r,k = II()

    # find the array of len == n lexigoraphycally smaller
    # such that &_i == ^_i and l <= ai <= r

    ## if n % 2 == 1 
    # then we can have all a_i == l
    # &_i == ^_i == l #so this is done
    # else:
    # 
    #

    if n == 2:
        print(-1)
    else:
        if n % 2 == 1:
            print(l)
        else:
            if 2**(int(math.log2(l)) + 1) <= r:
                if n - 1 <= k <= n:
                    print(2**(int(math.log2(l)) + 1))
                else:
                    print(l)
            else:
                print(-1)
 

    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
