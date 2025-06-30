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
    #idk honestly
    # maybe check if the ball is in the same direction  and on the same trajectory

    n,s = II()

    balls = [LI() for _ in range(n)]

    sol = 0 

    for i in range(n):
        if balls[i][2] + balls[i][3] == s and  ((balls[i][0] == -1 and balls[i][1] == 1) or (balls[i][0] == 1 and balls[i][1] == -1)) or \
        balls[i][2] == balls[i][3] and ((balls[i][0] == 1 and balls[i][1] == 1) or (balls[i][0] == -1 and balls[i][1] == -1)):
            sol += 1
        else:
            for j in range(i + 1, n):

                # symmetric trough origin
                if balls[i][1] == balls[j][1] and balls[i][0] == balls[j][0] and \
                   balls[i][2] == balls[j][3] and balls[i][3] == balls[j][2]:
                    sol += 2
                    break

            
                # symmetric trough other axis

    print(sol)

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

MULTI = True 
if __name__ == '__main__':
    main()