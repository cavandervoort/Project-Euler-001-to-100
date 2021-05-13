# Problem 67
# Maximum path sum II

f = open("p067_triangle.txt", "r")
pyramid = []
while True:
    line_temp = f.readline()
    new_row = line_temp.split(' ')
    if line_temp == '':
        break
    shave_last = new_row.pop(-1)
    new_row.append(shave_last[:-1])
    new_row_int = [int(x) for x in new_row]
    pyramid.append(new_row_int)

for row in range(98,-1,-1):
    for spot in range(row+1):
        pyramid[row][spot] += max([pyramid[row+1][spot], pyramid[row+1][spot+1]])

print(pyramid[0][0])
