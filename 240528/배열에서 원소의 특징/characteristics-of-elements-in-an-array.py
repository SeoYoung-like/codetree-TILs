arr = list(map(int, input().split()))

for i in range(10):
    if arr[i] % 3 == 0:
        if i == 0:
            print(arr[0])
        else:
            print(arr[i-1])
        break