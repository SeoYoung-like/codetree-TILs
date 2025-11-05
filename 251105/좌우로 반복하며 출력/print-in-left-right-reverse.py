n = int(input())
arr = [i + 1 for i in range(n)]

for _ in range(n):
    for i in range(n):
        print(arr[i], end="")
    print()
    arr.reverse()
