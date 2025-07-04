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
    # l,r 
    # find the max value of c 
    # where c is calculated as 
    # let a,b,c be three distinct numbers in the range [l,r]
    # c = (a ^ b) + (b ^ c) + (c ^ a)


    # 11111111    # 2 uguali e 1 diverso
    # 00000000 -> # 
    # 11111111    #

    # 0 1 1 
    # 

    # trovare 3 interi tali che in binario 
    # a[i][0] == a[i][1] != a[i][2]
    # a b
    # se non esistono? 

    l, r = II()
    a,b = l, r
    sol = 0
    flip = False

    # focus on the first MSB 

    for i in range(29, -1 , -1):
        if flip:
            if ((a >> i) & 1) == ((b >> i) & 1) and ((a >> i) & 1) == 0:
                a += (1 << i)
            elif ((a >> i) & 1) == ((b >> i) & 1) and ((a >> i) & 1) == 1:
                b -= (1 << i)

        if ((a >> i) & 1) != ((b >> i) & 1):
            flip = True



    if l <= a + 1 <= r and a + 1 != b:
        print(a, a + 1,b)
    elif l <= a - 1 <= r and a - 1 != b:
        print(a - 1, a, b)
    elif l <= b + 1 <= r and a != b + 1:
        print(a, b + 1, b)
    elif l <= b - 1 <= r and a != b - 1:
        print(a, b - 1, b)
    

    return
    
            
            
def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

MULTI = True 
if __name__ == '__main__':
    main()