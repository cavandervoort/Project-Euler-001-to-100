# Problem 63

def is_count(base,exp):
    num = base ** exp
    num_list = [dig for dig in str(num)]
    return len(num_list) == exp

count = 0
for base in range(1,10):
    exp = 1
    while True:
        if is_count(base,exp):
            count += 1
            exp += 1
        else:
            break
print(count)
