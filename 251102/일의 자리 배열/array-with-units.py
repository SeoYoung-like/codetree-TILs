n1, n2 = map(int, input().split())

print(n1, end=" ")
print(n2, end=" ")
for _ in range(8):
    n3 = n1 + n2
    print(n3 % 10, end=" ")
    n1 = n2
    n2 = n3
