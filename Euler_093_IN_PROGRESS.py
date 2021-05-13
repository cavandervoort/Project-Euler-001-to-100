# Problem 93
'''
126 combos of digits
24 orders for each set of numbers
64 combo/orders for operations
6 arrangements of parens

'''

def get_orders(a,b,c,d):
    dig_list = [a,b,c,d]
    orders = []
    for w in range(4):
        for x in range(3):
            for y in range(2):
                temp_list = [x for x in dig_list]
                new_order = []
                new_order.append(temp_list.pop(w))
                new_order.append(temp_list.pop(x))
                new_order.append(temp_list.pop(y))
                new_order.append(temp_list.pop(0))
                orders.append(new_order)
    return orders

digits = []
for a in range(1,10):
    for b in range(a+1,10):
        for c in range(b+1,10):
            for d in range(c+1,10):
                digits.append((a,b,c,d))

print(len(digits))

ops_dic = {'add':+, 'sub':-, 'mul':*, 'div':/}
ops = ['add','sub','mul','div']
ops_orders = []
for e in range(4):
    for f in range(4):
        for g in range(4):
            ops_orders.append((ops[e],ops[f],ops[g]))

print(ops_orders)

for digit_set in digits:
    digit_set_orders = get_orders(a,b,c,d)

 

