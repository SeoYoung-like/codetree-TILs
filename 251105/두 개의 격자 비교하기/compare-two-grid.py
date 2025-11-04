n, m = map(int, input().split())

arr1 = []
for _ in range(n):
    data = list(map(int, input().split()))
    arr1.append(data)

arr2 = []
for _ in range(n):
    data = list(map(int, input().split()))
    arr2.append(data)


for i in range(n):
    for j in range(m):
        if arr1[i][j] == arr2[i][j]:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()