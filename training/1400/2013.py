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
    # this code is a shame

    # practically 

    # first approach is naive : 

    # 2*n + 2 queries are enough to find the combination
    # if at a certain point neither 0 or 1 are the right answer that means
    # u should add to the back of the string if u are guessing like this 1010X
    # otherwise u should add to the front X1010 -> 1010X
    # total cost is 2*n + 2

    # in what way we can optimize this?

    # notice that if u can save one trie if the string is of length >= 2

    # instead of guessing 1 -> 0 -> 01 -> 00 we can save one query
    # if we query 01 and 10
    # or we get it and we save 2 or 3 queries 
    # or that means there are only 0 or 1 in the string
    # so if we send 11 or 00 we can save one query if 11 fail -> 00 is the string
    # otherwise is the specular 


    n = I()

    guess = "" if n == 1 else "0"
    back = False

    for _ in range(n):
        if len(guess) == n:
            break

        to_send = ""

        if len(guess) == 1:
            print("? " + guess + "1", flush=True)
            response = input().strip()
            if response == "0":
                print("? " + "1" + guess, flush=True)
                response = input().strip()
                if response == "1":
                    guess = "10"
                else:
                    print("? " + "11", flush=True)
                    response = input().strip()
                    if response == "0":
                        guess = "00"
                    else:
                        guess = "11"                
            else:
                guess = "01"
        else:
            if back:
                to_send = "0" + guess
            else:
                to_send = guess + "0"


            print("? " + to_send, flush=True)
            response = input().strip()

            if response == "0":
                if back:
                    to_send = "1" + guess
                else:
                    to_send = guess + "1"

                print("? " + to_send, flush=True)

                response = input().strip()

                if response == "0":
                        back = True
                else:
                    if back:
                        guess = "1" + guess
                    else:
                        guess += "1"

            elif response == "1":
                if back:
                    guess = "0" + guess
                else:
                    guess += "0"


    if len(guess) < n:
        print("! " + "1" + guess, flush=True)
    else:
        print("! " + guess, flush=True)

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

MULTI = True 
if __name__ == '__main__':
    main()