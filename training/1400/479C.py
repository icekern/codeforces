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

    n = I()
    exams = [tuple(II()) for _ in range(n)]
    exams.sort(key=lambda x: (x[0], x[1]))
    
    day = 0

    for start, end in exams:
        if day <= end:
            day = end
        else:
            day = start
    print(day)

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

MULTI = False 
if __name__ == '__main__':
    main()