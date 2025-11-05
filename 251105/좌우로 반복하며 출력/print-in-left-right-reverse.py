n = int(input())
arr = [i + 1 for i in range(n)]

for _ in range(4):
    for i in range(4):
        print(arr[i], end="")
    print()
    arr.reverse()
    