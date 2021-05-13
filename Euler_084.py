# Problem 84
# Monopoly odds

'''
Plan: start with odds of 2.5% per square, then iterate a bunch(100 times maybe), 
and see what the odds are. Each time, multiply the odds of being on a square with 
the odds of landing on a square from the original square and add it to the next 
round of odds for each square.

This works to find the most common squares, but the percentages don't perfectly line up. I 
think that some error is due to CHs that send you to CCs (36 back 3 to 33), but I don't feel
like coding that right now, and I'm not sure if that's the entire difference.
'''

starting_odds = [2.5]*40 

temp_odds = [0]*40
turns_total = 1000
dice_sides = 4
rolls = [0]*(2*dice_sides+1)
for x in range(1,dice_sides+1):
    for y in range(1,dice_sides+1):
        rolls[x+y] += 1/(dice_sides ** 2)

cc = [2, 17, 33]   
ch = [7, 22, 36]

for turn in range(turns_total):
    temp_odds = [0]*40
    for sqr in range(len(starting_odds)):
        for num in range(len(rolls)):
            
            # Go to Jail (square 30; 100% chance)
            if (sqr + num) % 40 == 30:
                temp_odds[10] += rolls[num] * starting_odds[sqr]
            
            # Community Chest (squares 2, 17, 33; 2/16 chance)
            elif (sqr + num) % 40 in cc:
                # Advance to GO (sqr 0)
                temp_odds[0] += rolls[num] * starting_odds[sqr] * (1/16)
                # Go to JAIL (sqr 10)
                temp_odds[10] += rolls[num] * starting_odds[sqr] * (1/16)
                # Else
                temp_odds[(sqr + num) % 40] += rolls[num] * starting_odds[sqr] * (14/16)
            
            # Chance (squares 7, 22, 36; 10/16 chance)
            elif (sqr + num) % 40 in ch:
                
                # Advance to GO (sqr 0)
                temp_odds[0] += rolls[num] * starting_odds[sqr] * (1/16)
                # Go to JAIL (sqr 10)
                temp_odds[10] += rolls[num] * starting_odds[sqr] * (1/16)
                # Go to C1 (sqr 11)
                temp_odds[11] += rolls[num] * starting_odds[sqr] * (1/16)
                # Go to E3 (sqr 24)
                temp_odds[24] += rolls[num] * starting_odds[sqr] * (1/16)
                # Go to H2 (sqr 39)
                temp_odds[39] += rolls[num] * starting_odds[sqr] * (1/16)
                # Go to R1 (sqr 5)
                temp_odds[5] += rolls[num] * starting_odds[sqr] * (1/16)
                # Go to next R (railway company) (x2) (sqr varies)
                if (sqr + num) % 40 == 7:
                    # Go to R2 (sqr 15)
                    temp_odds[15] += rolls[num] * starting_odds[sqr] * (2/16)
                elif (sqr + num) % 40 == 22:
                    # Go to R2 (sqr 25)
                    temp_odds[25] += rolls[num] * starting_odds[sqr] * (2/16)
                elif (sqr + num) % 40 == 36:
                    # Go to R2 (sqr 5)
                    temp_odds[5] += rolls[num] * starting_odds[sqr] * (2/16)
                # Go to next U (utility company) (sqrs 12 & 28)
                if (sqr + num) % 40 == 7 or (sqr + num) % 40 == 36:
                    # Go to U2 (sqr 12)
                    temp_odds[12] += rolls[num] * starting_odds[sqr] * (1/16)
                elif (sqr + num) % 40 == 22:
                    # Go to R2 (sqr 28)
                    temp_odds[28] += rolls[num] * starting_odds[sqr] * (1/16)
                # Go back 3 squares.
                temp_odds[sqr-3] += rolls[num] * starting_odds[sqr] * (1/16)
                # Else
                temp_odds[(sqr + num) % 40] += rolls[num] * starting_odds[sqr] * (6/16)

            else:
                temp_odds[(sqr + num) % 40] += rolls[num] * starting_odds[sqr]
    
    #forgotten go-to jails
    temp_odds[10] += temp_odds[30]
    temp_odds[30] = 0
    
    starting_odds = [x for x in temp_odds] 

value_dict = {}
for x in range(40):
    value_dict[x] = starting_odds[x]

value_arr = sorted(value_dict.items(), key=lambda item: item[1])
answer = str(value_arr[-1][0]) + "_" + str(value_arr[-2][0]) + "_" + str(value_arr[-3][0])
print(answer)
