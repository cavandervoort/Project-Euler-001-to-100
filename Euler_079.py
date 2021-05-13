# Problem 79
# Passcode derivation

def code_test(password,key_logs):
    for log in key_logs:
        first = False
        second = False
        third = False
        for num in password:
            if first == False:
                if num == log[0]:
                    first = True
                    continue
            if first == True and second == False:
                if num == log[1]:
                    second = True
                    continue
            if second == True:
                if num == log[2]:
                    third = True
                    break
        if third == False:
            print(f'Failed. {log} not found in {password}')
            return False
    
    print(f'Password: {password}')
    return True

f = open("p079_keylog.txt", "r")
key_logs = []
while True:
    line_temp = f.readline()
    if line_temp == '':
        break
    new_log = [x for x in line_temp]
    key_logs.append(new_log[:-1])

digits = ['0', '1', '2', '3', '6', '7', '8', '9']

p_num = 73162890
password = [x for x in str(p_num)]

code_test(password,key_logs)
