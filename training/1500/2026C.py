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
    # n action figures
    # i- th cost i coins avaible on the suffix [i,n]
    # binary string whether he can buy the i-th day
    # if he buys two action figures one is free max(a[....k])
    # he can buy one action figure and only one

    # dp ? no  -> vector in to know what he can buy
    # greedy? 
    # binary search? on the prize? -> 
     
    # greedy -> how 
    # inverte the order of the days ->
    # iff if he can buy the best he can do is buy the last one and the firs one 

    # ez 
    
    n  = I()
    s = input().strip()
    sol = 0

    perm_1 = deque([(i) for i in range(1,n + 1) if s[i - 1] == '1'])
    perm_0 = [(i) for i in range(1,n + 1) if s[i - 1] == '0']
    
    while perm_1:
        while perm_0 and perm_0[-1] > perm_1[-1]:
            sol += perm_0.pop()
        if perm_0:
            sol += perm_0.pop()
            perm_1.pop()
        else:
            if len(perm_1) == 1:
                sol += perm_1[-1]
                perm_1.pop()
            else:
                sol += perm_1.popleft()
                perm_1.pop()

    print(sol + sum(perm_0))
    
    
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