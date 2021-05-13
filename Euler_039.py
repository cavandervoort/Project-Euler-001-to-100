# Problem 39
# Integer right triangles

pMax = 0
solMax = 0

for p in range(841):
    solCount = 0
    for c in range(round(p/3), round(p/2)):    
        for b in range(round(p*0.29), c):       
            a = p - c - b
            if a > b:
                continue
            
            elif c ** 2 == a ** 2 + b ** 2:
                solCount += 1
    
    if solCount > solMax:
        solMax = solCount
        pMax = p

print(f'The p value with the max solutions is {pMax}')
