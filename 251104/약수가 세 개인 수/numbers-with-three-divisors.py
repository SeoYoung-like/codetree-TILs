start, end = map(int, input().split())

count = 0
for i in range(start, end):
    for j in range(2, i):
        if i % j == 0:
            if i == j * j:
                count += 1
            break
print(count)