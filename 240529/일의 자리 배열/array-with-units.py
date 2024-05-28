pp, p = map(int, input().split())

print(pp, p, sep=' ', end=' ')
for _ in range(8):
    tmp = (pp + p) % 10
    pp = p
    p = tmp
    print(tmp, end=' ')