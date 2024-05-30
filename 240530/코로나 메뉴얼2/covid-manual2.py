arr = [0, 0, 0, 0, '']
for _ in range(3):
    status, temp = input().split()
    temp = int(temp)

    if temp >= 37:
        if status =='Y':
            arr[0] += 1
        else:
            arr[1] += 1
    elif status == 'Y':
        arr[2] += 1
    else:
        arr[3] += 1

if arr[0] >= 2:
    arr[4] = 'E'

for elem in arr:
    print(elem, end=' ')