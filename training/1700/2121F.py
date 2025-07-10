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
# failed

def solve(_ = 0):
    
    
        
    n, s, x = II()
    a = LI()
    sol = 0
    dic = defaultdict(list)

    pfx = [0] * n

    blocks = []
    mas = []

    for i in range(n):
        if i == 0:
            pfx[i] = a[i]
            if a[i] == x:
                mas.append(i)

        if i > 0:

            if a[i] == x:
                mas.append(i)

            if a[i] > x:
                pfx[i] = int(1e300)
                blocks.append(i)
            else:
                if pfx[i - 1] == int(1e300):
                    pfx[i] = a[i]
                else:
                    pfx[i] = pfx[i - 1] + a[i]

    for i in range(n):
        dic[pfx[i]].append(i)

    b_p = 0
    m_p = 0

    for i in range(n):
        to_find = s + (pfx[i - 1] if i > 0 and pfx[i - 1] != int(1e300)  else 0)

        if to_find in dic:

            next_block = blocks[b_p] if b_p < len(blocks) else n
            next_mas = mas[m_p] if m_p < len(mas) else n

            lower_bound = bisect.bisect_left(dic[to_find], next_mas)
            upper_bound = bisect.bisect_left(dic[to_find], next_block)

            if lower_bound == n:
                continue
            if next_block == n:
                upper_bound = len(dic[to_find])

            if lower_bound < upper_bound:
                sol += upper_bound - lower_bound

        if  b_p < len(blocks) and i >= blocks[b_p]:
            b_p += 1
        if  m_p < len(mas) and i >= mas[m_p]:
            m_p += 1

    PRI(sol)


def main():
    if MULTI:
        for _ in range(I()):
            solve(_)
    else:
        solve()

if __name__ == '__main__':
    main()
