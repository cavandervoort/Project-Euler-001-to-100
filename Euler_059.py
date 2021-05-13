# Problem 59

f = open("p059_cipher.txt", "r")
crypted_list_ord_str = f.readline().split(',')
crypted_list_ord_int = [int(num) for num in crypted_list_ord_str]

diggy = 0
decoded_list_ord = []
while crypted_list_ord_int != []:
    if diggy % 3 == 0:
        temp_dig = crypted_list_ord_int.pop(0)
        decoded_list_ord.append(temp_dig ^ 101)
    elif diggy % 3 == 1:
        temp_dig = crypted_list_ord_int.pop(0)
        decoded_list_ord.append(temp_dig ^ 120)
    elif diggy % 3 == 2:
        temp_dig = crypted_list_ord_int.pop(0)
        decoded_list_ord.append(temp_dig ^ 112)
    diggy += 1

decoded_list_chr = [chr(num) for num in decoded_list_ord]
decoded_str = ''.join(decoded_list_chr)
print(decoded_str)

summy = 0
for num in decoded_list_ord:
    summy += num 
print(summy)
