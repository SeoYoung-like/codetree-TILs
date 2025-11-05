n = int(input())
arr = [i + 1 for i in range(n)]
copy_arr = arr.copy()
extend_arr = []

for i in range(n):
    extend_arr.append(copy_arr)
    arr.reverse()
    copy_arr = arr.copy()

for i in range(n):
    for j in range(n):
        print(extend_arr[j][i], end="")
    print()
