three_count = 0
five_count = 0
for _ in range(10):
    n = int(input())
    if n % 3 == 0:
        three_count += 1
    if n % 5 == 0:
        five_count += 1

print(f"{three_count} {five_count}")