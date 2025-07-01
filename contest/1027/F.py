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
    # factorization of x in tuple (factor, exponent)
    # interesting problem

    x,y,k = II()

    factors_x = defaultdict(int)

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:

            count = 0
            while x % i == 0:
                x //= i
                count += 1
            factors_x[i] = count
    if x > 1:
        factors_x[x] = 1



        
    factors_y = defaultdict(int)

    for i in range(2, int(math.sqrt(y)) + 1):
        if y % i == 0:
            count = 0
            while y % i == 0:
                y //= i
                count += 1
            factors_y[i] = count

    if y > 1:
        factors_y[y] = 1

    residual_factors = []

    for factor, exponent in factors_x.items():
        residual_factors.append((factor, factors_y[factor] - exponent))

    for factor, exponent in factors_y.items():
        if factor not in factors_x:
            residual_factors.append((factor, -exponent))

    sol = 0
    
    print(residual_factors)


    for factor, exponent in residual_factors:
        if k >= factor or exponent == 0:
            # find the maximum exponent that can be achieved with k
            if exponent == 0:
                continue

            temp_sub = 0
            temp_factor = factor

            while k >= temp_factor:
                temp_sub += 1
                temp_factor *= factor
            
            sol += abs(exponent) // temp_sub + (1 if abs(exponent) % temp_sub != 0 else 0)
        else:
            sol = -1
            break

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