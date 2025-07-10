from sys import stdin
input = lambda: stdin.readline().rstrip()
from collections import defaultdict

# by smilences 
# not mine

def solve():
    n, s, x = map(int, input().split())
    a = list(map(int, input().split()))
    d, q = defaultdict(int), []
    ans, acc = 0, 0
    for i in a:
        if i > x:
            d.clear()
            q.clear()
            continue

        q.append(acc)
        acc += i
        if i == x:
            for j in q:
                d[str(j)] += 1
            q.clear()
        ans += d[str(acc - s)]

    return ans

for _ in range(int(input())):
    print(solve())