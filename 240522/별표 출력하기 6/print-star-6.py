n = int(input())

cnt = 0
for i in range(1, n * 2):
    for _ in range(cnt):
        print(' ', end=' ')
    for _ in range(n * 2 - cnt * 2 - 1):
        print('*', end=' ')
    print()

    if i < n:
        cnt += 1
    else:
        cnt -= 1