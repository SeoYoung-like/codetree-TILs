n = int(input())

total = 0
for i in range(1, 100 + 1):
    total += i
    if total >= n:
        print(i)
        break
    