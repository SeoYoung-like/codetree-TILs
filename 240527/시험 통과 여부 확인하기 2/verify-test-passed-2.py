n = int(input())
cnt = 0

for _ in range(n):
    score_arr = list(map(int, input().split()))
    
    if sum(score_arr) / 4 >= 60:
        print("pass")
        cnt += 1
    else:
        print("fail")

print(cnt)