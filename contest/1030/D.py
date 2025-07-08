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
    
    n,k = II()
    traffic_lights = LI()
    delays = LI()
    q = I()
    starting_points = LI()

    #  strip that is long 10 ^ 15 
    #  there are n traffic lights
    #  each traffic light show red on  di under modulo k 
    #  given positions now, find if u can leave the strip in 10^100 seconds
    #  find a cycle in a graph practically
    #  or find that there is too much time to leave the strip
    #  let i be a node rapresenting the traffic light i
    #  let j be a node rapresenting the traffic light j
    #  there are 3 possibilities
    #  1. from there is a path from i to the end 
    #  2. from there is a path from i to the start
    #  3. u catch another traffic light in the middle 

    #  how u can do this 
    #  u know that u care only about the modulo k 
    #  under this modulo u know that u are gonna hit the traffic light if 
    #  (starting_point + seconds)% k == delays[i] 
    #  this cost O(n) -> 
    #  now u are gonna check if u hit the traffic light 
    #  if yes every traffic light is gonna have 2 edges for every direction
    #  after that u hit a traffic light u explore the graph but u can do a precalculation
    #  if there is a cycle in the graph u are infinitely stuck
    #  else
    #  u can leave in left_time[i]


    # creation the graph

    graph = defaultdict(list)

    for i in range(n):
        graph[i] = [[], []]

    for i in range(n):
        for j in range(i + 1, n):
            if (delays[i] + abs(traffic_lights[i] - traffic_lights[j])) % k ==  delays[j]:
                graph[i][1].append(j)
                break

        for j in range(i - 1, -1, -1):
            if (delays[i] + abs(traffic_lights[i] - traffic_lights[j])) % k ==  delays[j]:
                graph[i][0].append(j)
                break

    disty = [0] * n 

    # letz do n bfs

    # for every query q * n -> riducable with a matrix of modulus 
    # do n bfs calculate if i enter the node i how many seconds it takes to leave the strip


    def bfs(start,orientation):
        visited = [[False,False] for i in range(n)]
        solution = int(1e100 + 1)
        queue = deque([(start, 0, orientation)])
    
        while queue:
            current, seconds, orientation = queue.popleft()

            if visited[current][orientation]:
                continue

            visited[current][orientation] = True

            if graph[current][orientation] == []:
                if orientation == 0:
                    solution = min(solution, seconds + traffic_lights[current])
                else:
                    solution = min(solution, seconds + (int(10^15) - traffic_lights[current]))

            flipped_orientation = 1 - orientation

            for neighbor in graph[current][orientation]:    
                if not visited[neighbor][flipped_orientation]:
                    queue.append((neighbor, seconds + abs(traffic_lights[current] - traffic_lights[neighbor]) , flipped_orientation))

        return solution
    
    for i in range(n):
        disty[i] = bfs(i, 0)

    for i in range(q):
        starting_point = starting_points[i]
        flag = False

        for j in range(n):
            if starting_point <= traffic_lights[j] and abs(starting_point - traffic_lights[j]) % k == delays[j]:
                flag = True
                sol = "yes" if disty[j] < int(1e100 + 1) else "no"
                PRI(sol)
                break

        if not flag:
            PRI("yes")

    pass

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
