# Problem 61 
# Cyclical figurate numbers

import time
start = time.time()

triangle_list = []
n = 1
triangle = 1
while triangle < 10_000:
    triangle_list.append(triangle)
    n += 1
    triangle = int(n * (n + 1) / 2)
triangle_set = set(triangle_list)

square_list = []
n = 1
square = 1
while square < 10_000:
    square_list.append(square)
    n += 1
    square = int(n * n)
square_set = set(square_list)

pentagon_list = []
n = 1
pentagon = 1
while pentagon < 10_000:
    pentagon_list.append(pentagon)
    n += 1
    pentagon = int(n * (3 * n - 1) / 2)
pentagon_set = set(pentagon_list)

hexagon_list = []
n = 1
hexagon = 1
while hexagon < 10_000:
    hexagon_list.append(hexagon)
    n += 1
    hexagon = int(n * (2 * n - 1))
hexagon_set = set(hexagon_list)

heptagon_list = []
n = 1
heptagon = 1
while heptagon < 10_000:
    heptagon_list.append(heptagon)
    n += 1
    heptagon = int(n * (5 * n - 3) / 2)
heptagon_set = set(heptagon_list)

octagon_list = []
n = 1
octagon = 1
while octagon < 10_000:
    octagon_list.append(octagon)
    n += 1
    octagon = int(n * (3 * n - 2))
octagon_set = set(octagon_list)

for a in range(10,100):
    for b in range(10,100):
        ab = int(str(a)+str(b))
        if ab in octagon_set:       # only 40 ab combos are in the octagon set

            for c in range(10,100):
                bc = int(str(b)+str(c))
                for w in range(5):
                    set_list_1 = [triangle_set, square_set, pentagon_set, hexagon_set, heptagon_set] # resets set list
                    temp_set = set_list_1.pop(w)
                    if bc in temp_set:
                        
                        for d in range(10,100):
                            cd = int(str(c)+str(d))
                            for x in range(4):
                                set_list_2 = [listy for listy in set_list_1] # resets set list
                                temp_set = set_list_2.pop(x)
                                if cd in temp_set:

                                    for e in range(10,100):
                                        de = int(str(d)+str(e))
                                        for y in range(3):
                                            set_list_3 = [listy for listy in set_list_2] # resets set list
                                            temp_set = set_list_3.pop(y)
                                            if de in temp_set:
        
                                                for f in range(10,100):
                                                    ef = int(str(e)+str(f))
                                                    for z in range(2):
                                                        set_list_4 = [listy for listy in set_list_3] # resets set list
                                                        temp_set = set_list_4.pop(z)
                                                        if ef in temp_set: 
                                            
                                                            fa = int(str(f)+str(a))
                                                            if fa in set_list_4[0]:
                                                                print(ab+bc+cd+de+ef+fa)
                                            
print(f'Done in {time.time() - start} seconds')
