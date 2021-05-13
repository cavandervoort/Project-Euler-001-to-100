# Problem 82
# Path sum: three ways
import time
start = time.time()
print("This will take ~5 seconds")

def get_matrix():
    f = open("p082_matrix.txt", "r")
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
matrix.append([3,9,1,1,1,9])
matrix.append([3,9,1,9,1,9])
matrix.append([1,1,1,9,2,9])
matrix.append([9,9,9,9,1,9])
matrix.append([9,9,9,9,2,1])
matrix.append([9,9,9,9,2,1])


matrix = get_matrix()

matrix_running = [ [0]*len(matrix) for _ in range(len(matrix))]

# for x in range(len(matrix_running)):
#     print(matrix_running[x])

for pos in range(0,len(matrix)):
    for destination_row in range(0,len(matrix)):
        temp_min = 10 ** 20
        
        for origin_row in range(0,len(matrix)):
            
            if origin_row == destination_row:
                temp_min = min(temp_min, matrix_running[origin_row][pos-1]) 
            
            elif origin_row < destination_row:
                test = matrix_running[origin_row][pos-1]
                for add_row in range(origin_row+1, destination_row+1):
                    test += matrix[add_row][pos-1]
                temp_min = min(temp_min, test)
                
            elif origin_row > destination_row:
                test = matrix_running[origin_row][pos-1]
                for add_row in range(origin_row-1, destination_row-1, -1):
                    test += matrix[add_row][pos-1]
                temp_min = min(temp_min, test)
            
            else:
                print('ERROR')
        
        matrix_running[destination_row][pos] += temp_min + matrix[destination_row][pos]
          
min_path = 10 ** 20
for row in range(len(matrix)):
    if matrix_running[row][-1] < min_path:
        min_path = matrix_running[row][-1]

print(f'Min path is {min_path}')
print(f'Done in {time.time() - start} seconds')
