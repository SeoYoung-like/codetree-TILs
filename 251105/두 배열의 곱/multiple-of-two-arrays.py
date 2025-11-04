arr = [[], []]
for i in range(2):
    for _ in range(3):
        input_lst = list(map(int, input().split()))
        arr[i].append(input_lst)
    if i == 0:
        input()

# print(arr)

for i in range(3):
    for j in range(3):
        print(arr[0][i][j] * arr[1][i][j], end=" ")
    print()

