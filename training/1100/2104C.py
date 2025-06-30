# made by phone

#


t = int(input())
 
for _ in range(t):
    n = int(input())
    a = input()
 
    if (a[0] == 'A' and a[n - 1] == 'A') or \
       all(c == 'A' for c in a[:n - 1]) or \
       (a[n - 2] == 'A' and a[n - 1] == 'A'):
        print("Alice")
    else:
        print("Bob")