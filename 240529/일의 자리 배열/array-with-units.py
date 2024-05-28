pp, p = map(int, input().split())
arr = list()

arr.append(pp)
arr.append(p)

for i in range(8):
    arr.append((arr[i] + arr[i+1]) % 10)

for elem in arr:
    print(elem, end=' ')