# Problem 83
# Path sum: four ways

'''
Idea: Start with my solution to 81, then search for any improvements by going up, right, 
down, and left, until a full cycle has completed without any changes.

'''

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

matrix = get_matrix()

matrix_running = [ [10 ** 15]*len(matrix) for _ in range(len(matrix))]
matrix_running[0][0] = matrix[0][0]

row_count = len(matrix)
pos_count = len(matrix[0])
temp_final = 0
old_total_sum = 10 ** 12

for turn in range(1_000):
    for row in range(row_count):
        for pos in range(pos_count):
            up = 10 ** 15
            down = 10 ** 15
            right = 10 ** 15
            left = 10 ** 15

            if row != 0:
                up = matrix[row][pos] + matrix_running[row-1][pos]
            if row != row_count-1:
                down = matrix[row][pos] + matrix_running[row+1][pos]
            if pos != 0:
                left = matrix[row][pos] + matrix_running[row][pos-1]
            if pos != pos_count-1:
                right = matrix[row][pos] + matrix_running[row][pos+1]

            matrix_running[row][pos] = min(matrix_running[row][pos], up, down, left, right)
        
    temp_final = matrix_running[-1][-1]
    
    new_total_sum = 0
    for row in range(row_count):
        new_total_sum += sum(matrix_running[row])

    
    if old_total_sum == new_total_sum:
        break
    old_total_sum = new_total_sum

print(f'Answer: {matrix_running[-1][-1]}')

