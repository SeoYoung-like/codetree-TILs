A, B = map(int, input().split())

total = 0
for n in range(A, B+1):
    if n % 2 == 0:
        total += n

print(total)