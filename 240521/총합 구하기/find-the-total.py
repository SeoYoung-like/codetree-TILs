a, b = map(int, input().split())

sum_val = 0
for score in range(a, b+1):
    if score % 6 == 0 and score % 8 != 0:
        sum_val += score

print(sum_val)