str_list = {"apple", "banana", "grape", "blueberry", "orange"}
ch = input()

count = 0
for elem in str_list:
    print(elem)
    if elem[2] == ch:
        count += 1
    if elem[3] == ch:
        count += 1

print(count)