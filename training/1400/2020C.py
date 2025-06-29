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
    # b c d  
    # find a [0, 2^61] such that (a | b) - (a & c) = d
    
    # 10000000    
    # 10000101
    # 10000000

    b, c, d = II()

    not_possible = False
    a = 0
    for i in range(61, -1, -1):
        dig_b = (b >> i) & 1
        dig_c = (c >> i) & 1
        dig_d = (d >> i) & 1

        if dig_d == 1:
            if dig_b == 0 and dig_c == 1:
                not_possible = True
                break
            elif dig_b == 0 and dig_c == 0:
                a |= (1 << i)
        else:
            if dig_b == 1 and dig_c == 0:
                not_possible = True
                break
            elif dig_b == 1 and dig_c == 1:
                a |= (1 << i)

    if not_possible:
        print(-1)
    else:
        print(a)

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

MULTI = True 
if __name__ == '__main__':
    main()