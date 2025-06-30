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
    l1, b1, l2, b2, l3, b3 = II()

    if (l1 + l2 + l3 == b1 and b1 == b2 and b2 == b3) or (b1 + b2 + b3 == l1 and l1 == l2 and l2 == l3):
        print("YES")
    elif l3 + l2 == l1 and b3 == b2 and b3 + b1 == l1:
        print("YES")
    elif b3 + b2 == b1 and l3 == l2 and l3 + l1 == b1:
        print("YES")
    else:
        print("NO")

    # Write your solution here
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