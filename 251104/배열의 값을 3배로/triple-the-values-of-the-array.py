matrix = []
for _ in range(3):
    lst = list(map(int, input().split()))
    matrix.append(lst)


for i in range(3):
    for j in range(3):
        print(matrix[i][j] * 3, end="")
    print()