n = int(input())

cnt = 0
for y in range(1, n+1):
    if y % 4 == 0 and not(y % 100 == 0 and y % 400 != 0):
        cnt += 1

print(cnt)