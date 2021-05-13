# Problem 81
# Path sum: two ways

def get_matrix():
    f = open("p081_matrix.txt", "r")
    matrix = []
    while True:
        line_temp = f.readline()
        if line_temp == '':
            break
        list_temp = line_temp.split(',')
        list_temp[-1] = list_temp[-1][:-1]
        matrix.append([int(x) for x in list_temp])
    return matrix

matrix = []
matrix.append([3,1,4,5,9])
matrix.append([2,8,4,5,1])
matrix.append([3,1,4,5,2])
matrix.append([9,9,9,5,3])
matrix.append([3,1,4,2,9])

matrix = get_matrix()

# for x in range(len(matrix)):
#    print(matrix[x])
# print('')

for row in range(1,len(matrix)):
    matrix[row][0] += matrix[row-1][0]

for pos in range(1,len(matrix)):
    matrix[0][pos] += matrix[0][pos-1]    
    
# for x in range(len(matrix)):
#     print(matrix[x])
# print('')

for row in range(1,len(matrix)):
    for pos in range(1,len(matrix)):
         matrix[row][pos] += min(matrix[row-1][pos], matrix[row][pos-1])

# for x in range(len(matrix)):
#    print(matrix[x])            

print(matrix[-1][-1])
