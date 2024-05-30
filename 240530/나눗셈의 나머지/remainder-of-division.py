a, b = map(int, input().split())
arr = [0] * 10
ans = 0

while a > 1:
    arr[a % b] += 1
    a //= b

for elem in arr:
    ans = ans + elem ** 2

print(ans)