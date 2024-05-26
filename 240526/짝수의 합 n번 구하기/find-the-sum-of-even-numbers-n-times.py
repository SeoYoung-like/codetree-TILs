n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    sum_val = 0
    for curr_num in range(a, b+1):        
        if curr_num % 2 ==0:
            sum_val += curr_num
    print(sum_val)