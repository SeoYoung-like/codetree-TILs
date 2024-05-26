arr = list(map(int, input().split()))

sum_val = 0
cnt = 0
for elem in arr:
    if elem >= 250:
        break
    cnt += 1
    sum_val += elem

avg = int((sum_val / cnt) * 10 + 0.5) / 10
print(f"{sum_val} {avg}")