# Problem 99
# Largest exponential

def get_pairs(file_name, permissions): # gets coordinates from file and formats them
    
    f = open(file_name, permissions)
    pairs = []
    line_str = ' '
    while line_str != '':

        line_temp = f.readline()
        line_str = [char for char in line_temp]
        line_str = ''.join(line_str)
        if len(line_str) < 10:
            break
        
        line_list = line_str[0:].split(',')
        output = []
        for pos in range(len(line_list)):
            output.append(int(line_list[pos]))
        
        pairs.append(output)

    return pairs

def bigger_big(x,y,a,b):
    
    x_temp = x
    y_temp = y
    a_temp = a
    b_temp = b
    
    while True:
        if x_temp >= y_temp and a_temp >= b_temp:
            return (x,a)

        elif y_temp >= x_temp and b_temp >= a_temp:
            return (y,b)
        
        elif x_temp >= y_temp and b_temp >= a_temp:
            x_temp /= y_temp
            b_temp -= a_temp
        
        else:
            y_temp /= x_temp
            a_temp -= b_temp

pairs = get_pairs("p099_base_exp.txt", "r")

max_line = 1
x = pairs[0][0]
a = pairs[0][1]

for pair_num in range(1,len(pairs)):
    y = pairs[pair_num][0]
    b = pairs[pair_num][1]
    x,a = bigger_big(x,y,a,b)
    
    if x == y and a == b: # if the new pair became x and y
        max_line = pair_num + 1
    
print(f'The max value is line {max_line}, in which the base is {x} and the exponent {a}.')
