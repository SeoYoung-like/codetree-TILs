n = int(input())

cnt = 65
for i in range(1, n + 1):
    for _ in range(i):
        print(chr(cnt), end='')
        cnt += 1
        if cnt > ord('Z'):
            cnt = 65
    print()