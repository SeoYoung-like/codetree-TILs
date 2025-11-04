arr = []
for _ in range(4):
    data = list(map(int, input().split()))
    arr.append(data)

total = 0
for i in range(4):
    for j in range(4):
        if j <= i:
            total += arr[i][j]
print(total)