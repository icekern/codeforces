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
    a = input().strip()

    chars = [c for c in a]

    zeros = chars.count('0')
    ones = chars.count('1')
    
    # we have a string with 0s and 1s 

    # for every 0 we can form a pair so a +1 with another 0 
    # for every 1 we can form a pair so a +1 with another 1

    # if we want to form exactly k pairs 
    # we need at least k pairs between 0s and 1s and we need the rest to be alternable
    # so we need to check if the number of zeros and ones are enough for k 
    # and after that we need to check if we have sufficient 0s and ones to unbalanced the string 
    # how 
    # 1101011001
    # 1111110000
    #   000111
    # wtf?
    # 1110000111
    # if we have k pairs,
    # 1111110000
    # 1110000111
    # if we have k pairs we can obtain the string with k - 2 pairs
    # 


    possible_pairs = zeros // 2 + ones // 2
    minimun_pairs = min(zeros, ones)
    
    if k % 2 == possible_pairs % 2  and possible_pairs - minimun_pairs <= k:
        print('YES')
    else:
        print('NO')

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

MULTI = True 
if __name__ == '__main__':
    main()