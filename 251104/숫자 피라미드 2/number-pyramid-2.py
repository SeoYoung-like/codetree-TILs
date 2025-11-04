n = int(input())

count = 0
for i in range(n):
    for _ in range(0, i+1):
        count += 1
        print(count, end=" ")
    print()