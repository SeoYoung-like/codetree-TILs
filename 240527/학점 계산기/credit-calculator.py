n = int(input())
arr = list(map(float, input().split()))

avg = int((sum(arr) / n) * 10 + 0.5) / 10

print(avg)
if avg >= 4.0:
    print("Perfect")
elif avg >= 3.0:
    print("Good")
else:
    print("Poor")