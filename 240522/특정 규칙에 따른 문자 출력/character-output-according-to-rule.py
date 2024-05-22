n = int(input())

cnt = 0

for i in range(n):
    for _ in range(n - (i + 1)):
        print(' ', end=' ')
    for _ in range(i + 1):
        print('@', end=' ')
    print()

for i in range(1, n):
    for _ in range(n - i):
        print('@', end=' ')
    for _ in range(i):
        print(' ', end=' ')
    print()