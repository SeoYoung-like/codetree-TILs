n1, n2 = map(int, input().split())
arr = list()

arr.append(n1)
arr.append(n2)

for i in range(2, 10):
    arr.append(arr[i-1] + 2 * arr[i-2])

for elem in arr:
    print(elem, end=' ')