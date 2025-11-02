n = int(input())
lst = list(map(int, input().split()))

for item in reversed(lst):
    if item % 2 == 0:
        print(item, end=' ')

