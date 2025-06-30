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
    # n row m columns
    # every cells has a direction
    # ? unspecified
    # find the number of ways u can put the arrows in such a way that the number of starting cells from which rostam will be trapped forever is maximized
    # graph theory 
    # practically every time u can made a cycle u trap him
    # explore the matrix and find the number and the lenght of the cycles

    # first explore the matrix 
    # if a cell can expaxe expand to the ones that are pointing to it
    # if not then color it with 0
    # after that u should have a matrix with 0 , 1 and 2 for the unspecified cells
    # if a cell is 2 and it confines to a cells with 0 or 2 then it s impossible to start from them 
    # otherwise u can start from them

    # problem now how do i do the recursion in python? 

    n, m = II()
    matrix = [[c for c in input().strip()] for _ in range(n)]

    # U -> up
    # D -> down
    # L -> left
    # R -> right
    directions = {
        "U": (-1, 0),  # U
        "D": (1, 0),   # D
        "L": (0, -1),  # L
        "R": (0, 1)    # R
    }

    visited = [[0] * m for _ in range(n)]
    colors = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if visited[i][j] != 0:
                continue
            
            def dfs(x, y):

                if matrix[x][y] == "?":
                    return 

                if visited[x][y] != 0:
                    return
                
                visited[x][y] = 1

                dx, dy = directions.get(matrix[x][y])
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m:
                    if visited[nx][ny] == 0:
                        dfs(nx, ny)

                    # if we point to a cell that is out of bounds we get the same color    
                    if visited[nx][ny] == 1 and colors[nx][ny] == 1:
                        colors[x][y] = 1

                else:
                    # if we go out of bounds we can color it with 1
                    colors[x][y] = 1

            if matrix[i][j] != "?":
                dfs(i, j)

    # if a cell with ? is surrounded by 1 it should be colored with 1

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "?":
                # check the neighbors
                # get the neighbors
                neighbors = []

                for dx, dy in directions.values():
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        neighbors.append(colors[nx][ny])

                # if all the neighbors are 1 then color it with 1
                if all(color == 1 for color in neighbors):
                    colors[i][j] = 1

    print(n * m - sum(colors[i][j] == 1 for i in range(n) for j in range(m)))

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

MULTI = True 
sys.setrecursionlimit(10**4)
if __name__ == '__main__':
    main()