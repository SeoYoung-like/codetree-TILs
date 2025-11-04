arr = []
for _ in range(4):
    data = list(map(int, input().split()))
    arr.append(data)

for i in range(4):
    total = 0
    for j in range(4):
        total += arr[i][j]
    print(total)