# Problem 91
# Right triangles with integer coordinates

# Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?

import time
start = time.time()

print("This takes ~5 seconds")

def is_right(top_x,top_y,right_x,right_y):
    top_line_sqr = top_x ** 2 + top_y ** 2
    right_line_sqr = right_x ** 2 + right_y ** 2
    connect_line_sqr = (top_x-right_x) ** 2 + (top_y-right_y) ** 2
    if top_line_sqr * right_line_sqr * connect_line_sqr == 0:
        return False
    elif top_line_sqr + right_line_sqr == connect_line_sqr:
        return True
    elif top_line_sqr + connect_line_sqr == right_line_sqr:
        return True
    elif connect_line_sqr + right_line_sqr == top_line_sqr:
        return True
    else:
        return False

is_right(1,1,1,1)

height = 50
width = 50
count_right = 0

for top_y in range(height+1):
    for right_y in range(top_y+1):
        for right_x in range(width+1):
            for top_x in range(right_x+1):
                if is_right(top_x,top_y,right_x,right_y):
                    count_right += 1
                    # print(f'found one at ({top_x},{top_y}),({right_x},{right_y})')

print(f'Found a total of {count_right} right triangles in a {height}x{width} grid')
print(f'\nThis took {time.time() - start} seconds')
