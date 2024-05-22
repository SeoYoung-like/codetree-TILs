n = int(input())

toggle = True
for i in range(1, n+1):
    if toggle:
        print('*', end=' ')
    else: 
        for _ in range(i):
            print('*', end=' ')
    toggle = False if toggle else True
    print()