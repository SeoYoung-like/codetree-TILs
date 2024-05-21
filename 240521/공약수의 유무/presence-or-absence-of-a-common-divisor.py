a, b = map(int, input().split())

satisfied = False
for n in range(a, b + 1):
    if 1920 % n == 0 and 2880 % n == 0:
        satisfied = True

if satisfied == True:
    print(1)
else:
    print(0)