a, b = map(int, input().split())

arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while a != 0:
    arr[a % b] += 1
    a = a // b

ans = 0
for elem in arr:
    ans = ans + elem ** 2

print(ans)