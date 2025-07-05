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
    # rooted graph
    # d(v) smallest node label on the unique simple path from v to root
    #

    n,m = II()

    if n <= m <= n * (n + 1) // 2:
        f = set(range(1, n + 1))
        solutions = []

        for i in range(n, 0, -1):
            if i + i - 1 < m:
                solutions.append(i)
                f.discard(i)
                m -= i
            else:
                temp = i
                while temp + (i - 1) != m:
                    temp -= 1

                solutions.append(temp)
                f.discard(temp)
                if temp != 1:
                    solutions.append(1)
                    f.discard(1)
                    
                solutions.extend([x for x in f])
                break

        PRI(solutions[0])
        
        for i in range(len(solutions) - 1):
            PRI(str(solutions[i]) + " " + str(solutions[i + 1]))
        
    else:
        PRI(-1)
        return
    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
