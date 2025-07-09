import sys
from collections import defaultdict, deque
import math
import heapq
import bisect

def input(): return sys.stdin.readline().rstrip('\n')
def I(): return int(input())
def II(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def SI(): return input().split()
def PRI(*args, **kwargs):
    if DEBUG == 1:
        green = "\033[92m"
        reset = "\033[0m"
        print(f"{green}{kwargs.get('sep', ' ').join(map(str, args))}{reset}", **kwargs)
    else:
        print(*args, **kwargs)

DEBUG = 1
MULTI = True 

def solve():
    n = I()
    a = LI()
    b = LI()

    operations = []
    for i in range(1, n + 1):

        index_a = 0
        index_b = 0

        if i in b:
            index_a = b.index(i)
            a[index_a],b[index_a] = b[index_a], a[index_a]
            operations.append((3, index_a + 1))

        if i + n in a:
            index_b = a.index(i + n)
            a[index_b],b[index_b] = b[index_b], a[index_b]
            operations.append((3, index_b + 1))

        index_b = b.index(i + n)
        index_a = a.index(i)
        
        if index_b < b[index_b] - n - 1:
            for j in range(index_b,  b[index_b] - n - 1):
                operations.append((2, j + 1))
                b[j],b[j + 1] = b[j + 1], b[j]
        else:
            for j in range( index_b, b[index_b] - n - 1, -1):
                operations.append((2, j))
                b[j],b[j - 1] = b[j - 1], b[j]

        if index_a < a[index_a] - 1:
            for j in range(index_a, a[index_a] - 1):
                operations.append((1, j + 1))
                a[j],a[j + 1] = a[j + 1], a[j]
        else:
            for j in range(index_a, a[index_a] - 1, -1):
                operations.append((1, j))
                a[j],a[j - 1] = a[j - 1], a[j]
            
    PRI(len(operations))

    for op in operations:
        PRI(*op)
    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
