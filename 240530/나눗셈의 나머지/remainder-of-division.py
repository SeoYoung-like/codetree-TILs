a, b = map(int, input().split())

arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while True:
    division = a // b
    quot = a % b
    arr[quot] += 1
    if division == 0:
        break
    a = division        

ans = 0
for elem in arr:
    ans = ans + elem ** 2

print(ans)