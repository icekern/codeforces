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
    # i and j fight
    # after the fight a[j] -= a[i]
    # best strategy ? 

    # a[j] -= a[i] a[i] is eliminated
    # best strategy to maximize the last element remaining after the process

    # a[-1] is always the last remaining element
    # if a[j] < a[i] then a[j] is a surplus to a[-1]
    # if a[j] > a[i] then a[i] is a minus to a[-1]
    # due the fact that are all negative
    # is it good if we do a[-2] -= sum(a[:-2]) a[-1] -= a[-2]
    # does it work?

    # formally the process is:
    # a[j] -= a[i] negative  increasing a[-1] by a[j] is the same as 
    # subtracting a[j] and a[i] from a[-2] -> why r - x - y - k = r - (y - k) + x  

    n = I()
    a = LI()


    a[-2] -= sum(a[:-2])
    a[-1] -= a[-2]

    print(a[-1])


def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

MULTI = True 
if __name__ == '__main__':
    main()