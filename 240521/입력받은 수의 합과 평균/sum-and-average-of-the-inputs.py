n = int(input())

sum_val = 0

for _ in range(n):
    score = int(input())
    sum_val += score

print(f"{sum_val} {sum_val/n:.1f}")