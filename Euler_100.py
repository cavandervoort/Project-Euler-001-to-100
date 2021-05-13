# Problem 100

import math

blue = 1
total = 1
new_blue = 1
new_total = 1

while blue < 10 ** 13:
    win = 2 * blue * (blue - 1)
    lose = total * (total - 1)
    if win > lose:
        # print(f'WIN for {blue}/{total}')
        total += 1
    elif win < lose:
        # print(f'LOSE for {blue}/{total}')
        blue += 1
        # total += 1
    else:
        
        old_blue = new_blue
        old_total = new_total
        new_blue = blue
        new_total = total
        blue_ratio = new_blue/old_blue
        total_ratio = new_total/old_total
        
        blue = max(blue+1, math.floor(blue * blue_ratio) - 1)
        total = max(total+1, math.floor(total * total_ratio) - 1)
        if total > 10 ** 12:
            print(f'50/50 for blue: {blue} / total: {total}')
            break
        
     