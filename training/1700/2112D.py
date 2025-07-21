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

# https://github.com/icekern/codeforces

DEBUG = 1
MULTI = True 

def solve():
    n = I()

    graph = defaultdict(list)

    for _ in range(n - 1):
        u,v = II()
        graph[u].append(v)
        graph[v].append(u)


    grade = -1

    for i in range(1,n + 1):
        if len(graph[i]) == 2:
            grade = i
            break

    if grade != -1:

        q = deque()
        to_out = []
        visited = [False] * (n + 1)

        q.append((graph[grade][0], 1))
        to_out.append((graph[grade][0], grade))

        q.append((graph[grade][1], 0))
        to_out.append((grade, graph[grade][1]))

        visited[grade] = 1

        while q:
            node,direction = q.popleft()

            visited[node] = True
            for neigh in graph[node]:
                if not visited[neigh]:
                    q.append((neigh, not direction))
                    if not direction:
                        to_out.append((neigh,node))
                    else:
                        to_out.append((node,neigh))

        PRI('YES')

        for i in range(len(to_out)):
            PRI(*to_out[i])
    
    else:
        PRI('NO')

    pass
    

def main():
    if MULTI:
        for _ in range(I()):
            solve()
    else:
        solve()

if __name__ == '__main__':
    main()
