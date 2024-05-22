n = int(input())

for i in range(1, n * 2 + 1):
    if i % 2 == 0:
        for _ in range(n - (i//2 - 1)):
            print('*', end=' ')
    else:
        for _ in range(1 + i//2):
            print('*', end=' ')
    print()