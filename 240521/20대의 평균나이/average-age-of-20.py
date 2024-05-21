sum_val = 0
cnt = 0

while True:
    age = int(input())
    if age < 20 or age > 29:
        break
    sum_val += age
    cnt += 1

print(f"{sum_val/cnt:.2f}")