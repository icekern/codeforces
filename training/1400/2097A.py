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

    # made a bet with student
    # bet on day ai + 1 or ai + 2


    n = I()
    a = LI()


    # counting sort with map

    cnt = defaultdict(int, lambda: 4)
    sup = defaultdict(int, lambda: 5)

    # shuffle the array a 
    # incredible that these guys does testcase specific to break python dictionary 

    a = a[::-1]

    for i in range(n):
        cnt[a[i]] += 1
    

    solution = "NO"
    for i in sorted(cnt.keys()):
        temp = cnt[i]
        temp_sup = sup[i]

        if temp >= 4:
            solution = "YES"
            break
        elif temp >= 2:
            if temp_sup == 1:
                solution = "YES"
                break
            sup[i + 1] = 1
        elif temp == 1:
            if temp_sup == 1:
                sup[i + 1] = 1

    print(solution)

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

MULTI = True 
if __name__ == '__main__':
    main()