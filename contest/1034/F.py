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
    # a perm of lengh n is good if gcd(pi,i) > 1 for all i in [2,n]
    # find a good permutation with the minimum number of fixed points 
    # fixed points are the indices i such that pi = i

    # u are creating some cycles u can find this permutation by shifting the multiples of p 
    # by 1 is this a good idea? is this the minimum?

    # n log(n) for finding the primes

    # n for creating the permutation 

    # taking a index i in what places can i put it? in every place where pi / i > 1 
    # in every i that is a divisor of pi

    # it works 

    # for every prime p i save p * 2 


    n = I()
    perm = [0] * (n + 1)
    primes = set()
    eratosthenes = [True] * (n + 1)
    eratosthenes[0] = False

    dicz = defaultdict(list)

    for i in range(2, n + 1):
        if eratosthenes[i]:
            primes.add(i * 2)

            for j in range(i * 2, n + 1, i):
                if eratosthenes[j]:
                    eratosthenes[j] = False

    for e in primes:
        dicz[e//2].append(e//2)
        dicz[e//2].append(e)

    eratosthenes = [True] * (n + 1)
    eratosthenes[0] = False

    for i in range(2, n + 1):
        if eratosthenes[i]:
            for j in range(i * 2, n + 1, i):
                if eratosthenes[j]:
                    eratosthenes[j] = False
                    if not j in primes:
                        dicz[i].append(j)
    
    perm = [0] * (n + 1)
    perm[1] = 1

    for k in dicz.keys():
        if k > n:
            continue
        else:
            temp = 0
            for i in range(1,len(dicz[k])):
                if dicz[k][i] > n:
                    break
                temp = i
                perm[dicz[k][i-1]] = dicz[k][i]

            perm[dicz[k][temp]] = dicz[k][0]
            
    print(" ".join(map(str, perm[1:])))

def main():

    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

MULTI = True 
if __name__ == '__main__':
    main()