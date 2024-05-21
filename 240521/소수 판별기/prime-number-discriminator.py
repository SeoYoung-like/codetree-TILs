n = int(input())

satisfied = True
for c in range(2, n):
    if n % c == 0:
        satisfied = False

if satisfied == True:
    print('P')
else:
    print('C')