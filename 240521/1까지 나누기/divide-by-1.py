n = int(input())

cnt = 0
val = n

for i in range(1, n+1):
    val = int(val / i)
    cnt += 1
    if val <= 1:
        break

print(cnt)