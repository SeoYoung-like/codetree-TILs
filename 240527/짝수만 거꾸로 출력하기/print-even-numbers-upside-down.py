n = int(input())

arr = list(map(int, input().split()))
reversed_arr = list()

for elem in arr:
    if elem % 2 == 0:
        reversed_arr.append(elem)

for elem in reversed_arr:
    print(elem, end=' ')