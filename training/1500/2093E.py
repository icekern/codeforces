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
    n,k = II()
    a = LI()

    # given an array find the maximum value of mex(bi) 1 <= i <=k
    # where bi is a subarray of a 

    # starting with the zeros 
    # bruteforce -> 0 expand the array and find the mex of each subarray
    # what we can do 

    #  1 2 3 4 0| 0 1 2 3 | 0 1 2 3 
    # starting from the first subarray 
    # i continue to expand till finding another zero?
    # is it possible to do a dp? 

    # like dp[i][0 1 2] mmmmmm
    # nope no dp

    # it s greedy 

    # pigeonhole principle is another way if i have 3 k 
    # i should have at least 2 subarrays with 0 1 2 3 0 1 2 3 0 1 2 3 
    # splitting where the zeros are is not the solution sooo

    #  0 0 0 i want 2 for example
    #  0 0 1 1 0 0 2 2 0 0 1 1
    #  binary search ?
    #  crazy binary search ? 
    #  aaaaaaaaaaaaaa
    #  how can i find the mex of a sequence in O(1) time?
    #  nada it is possible with binary search letzgo  
    #  why it works? 

    l,r = -1, n // k 
    sol = 0
    while l < r:
        mid = (l + r + 1) // 2
        possible = False

        checklist = [[0] * (mid + 1) for _ in range(k)]

        j = 0
        total = 0
        for i in range(n):
            if a[i] <= mid and checklist[j][a[i]] == 0:
                total += 1
                checklist[j][a[i]] = 1
            if total == mid + 1:
                if j == k - 1:
                    possible = True
                    break
                j += 1
                total = 0
        if possible:
            l = mid
            sol = l + 1
        else:
            r = mid - 1
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