import sys

def solve():
    n, k = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()

    cnt0 = s.count('0')
    cnt1 = s.count('1')
    cnt2 = s.count('?')

    if cnt0 + cnt1 + cnt2 >= n:
        print('-' * n)
        return

    ans = ['+'] * n

    for i in range(cnt0):
        ans[i] = '-'
    for i in range(n - cnt1, n):
        ans[i] = '-'

    for i in range(cnt0, min(cnt0 + cnt2, n)):
        if ans[i] == '+':
            ans[i] = '?'
    for i in range(max(0, n - (cnt1 + cnt2)), n - cnt1):
        if ans[i] == '+':
            ans[i] = '?'

    print("".join(ans))


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()