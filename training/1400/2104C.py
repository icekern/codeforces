import sys
from collections import defaultdict, deque
import math
import heapq

def input(): return sys.stdin.readline().rstrip('\n')
def I(): return int(input())
def II(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def SI(): return input().split()

# Sieve of Eratosthenes to find all prime numbers up to 10^7
era = [0] * (10**7 + 1) 

for i in range(2, len(era)):
    if era[i] == 0:
        for j in range(i + i, len(era), i):
            era[j] = 1 

era[0] = 1
era[1] = 1

era = [i for i in range(len(era)) if era[i] == 0]

pfx = [0] * (len(era) + 1)

for i in range(1, len(era) + 1):
    pfx[i] = pfx[i - 1] + era[i - 1]
# This creates a prefix sum array of the prime numbers

def solve():
    # a vec size n 
    # operations:
    # pay 1 coin to increase any element by 1
    # gain 1 coin decrease any element by 1

    # an array is ideal if 
    # Vi a[i] >= 2  and  gcd(a[i],a[j]) = 1 for all i != j
    # you have no coins at the start 

    # this means that u can modify the array as u want for a quantity of sum(a)
    # minumun namber of elements to remove to make it ideal 

    # if i didn t have the conditions where i could remove elements it s easy
    # bcz i need to consider every array that respects this condition 
    # sum(a) = sum(v)
    
    # if i do eratostene 4 * 10 ^ 5  we pick every possible nunber and we put them in a vector 
    # we create a pfx of sum of the vector 
    # we order the vector of the elements of the problem 
    # and we remove elements until the sum is a[:i] >= era[i]

    n = I()
    a = LI()

    # eratostene

    a.sort()

    initial_sum = sum(a)

    for i in range(len(a), 0, -1):
        if pfx[i] <= initial_sum:
            sol = i
            break
        else:
            initial_sum -= a[n - i]

    print(len(a) - sol)  # number of elements to remove to make it ideal

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

MULTI = True 
if __name__ == '__main__':
    main()  