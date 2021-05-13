# Problem 43
# Sub-string divisibility

# get list of 2-3 numbers divisible by 17

num = 17
str_list_17 = []
while num < 1000:
    num_str = ''
    num_str += str(num)
    if len(num_str) < 3:
        num_str = '0' + num_str
    if len(set(num_str)) == 3:
        str_list_17.append(num_str)
    num += 17

str_list_13 = []
for num in str_list_17:
    for new_dig in range(10):
        if str(new_dig) in num:
            continue
        num_str = str(new_dig) + num[0:2]
        if int(num_str) % 13 == 0:
            str_list_13.append(str(new_dig) + num)

str_list_11 = []
for num in str_list_13:
    for new_dig in range(10):
        if str(new_dig) in num:
            continue
        num_str = str(new_dig) + num[0:2]
        if int(num_str) % 11 == 0:
            str_list_11.append(str(new_dig) + num)

str_list_7 = []
for num in str_list_11:
    for new_dig in range(10):
        if str(new_dig) in num:
            continue
        num_str = str(new_dig) + num[0:2]
        if int(num_str) % 7 == 0:
            str_list_7.append(str(new_dig) + num)

str_list_5 = []
for num in str_list_7:
    for new_dig in range(10):
        if str(new_dig) in num:
            continue      
        num_str = str(new_dig) + num[0:2]
        if int(num_str) % 5 == 0:
            str_list_5.append(str(new_dig) + num)

str_list_3 = []
for num in str_list_5:
    for new_dig in range(10):
        if str(new_dig) in num:
            continue
        num_str = str(new_dig) + num[0:2]
        if int(num_str) % 3 == 0:
            str_list_3.append(str(new_dig) + num)

str_list_2 = []
for num in str_list_3:
    for new_dig in range(10):
        if str(new_dig) in num:
            continue
        num_str = str(new_dig) + num[0:2]
        if int(num_str) % 2 == 0:
            str_list_2.append(str(new_dig) + num)

str_list_1 = []
for num in str_list_2:
    for new_dig in range(10):
        if str(new_dig) in num:
            continue
        num_str = str(new_dig) + num[0:2]
        if int(num_str) % 1 == 0:
            str_list_1.append(str(new_dig) + num)

sum_pan_interesting = 0
for num in str_list_1:
    sum_pan_interesting += int(num)

print(f'Answer: {sum_pan_interesting}')
