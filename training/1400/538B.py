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
    
    r = input().strip()

    digits = [int(c) for c in r]
    to_out = ""
    while not all(d == 0 for d in digits):
        number = 0
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 0:
                continue
            else:
                digits[i] -= 1
                number += 10 ** (len(digits) - i - 1)
        to_out += str(number) + " "

    print(len(to_out.strip().split(" ")))
    print(to_out.strip())

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

MULTI = False
if __name__ == '__main__':
    main()