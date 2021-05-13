# Problem 55
# Lychrel numbers

def is_lychrel(x):
    x_list,x_list_rev,x_rev = reverse_num(x)

    for cycle in range(50):
        x += x_rev
        x_list,x_list_rev,x_rev = reverse_num(x)
        
        if is_palin(x_list,x_list_rev):
            return False
        
        if cycle == 49:
            return True

def reverse_num(x):
    x_list = [dig for dig in str(x)]
    x_list_rev = [x_list[dig] for dig in range(len(x_list)-1,-1,-1)]
    x_rev = int(''.join(x_list_rev)) 
    return(x_list,x_list_rev,x_rev)

def is_palin(x_list,x_list_rev):
    return x_list == x_list_rev

count_lychrel = 0
limit = 10000
for num in range(1,limit+1):
    if is_lychrel(num) == True:
        count_lychrel += 1

print(f'{count_lychrel} Lychrels out of {limit} numbers') 
