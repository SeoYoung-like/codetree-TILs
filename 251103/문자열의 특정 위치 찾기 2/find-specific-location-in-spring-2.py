str_list = {"apple", "banana", "grape", "blueberry", "orange"}
ch = input()

count = 0
is_num = False
for elem in str_list:
    if elem[2] == ch:
        count += 1
        is_num = True
    if elem[3] == ch:
        count += 1
        is_num = True
    if is_num:
        print(elem)
        is_num = False

print(count)