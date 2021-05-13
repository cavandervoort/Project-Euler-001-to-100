# Problem 54
# Poker hands

convert_list = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

def split(hand):
    shift = 0
    hands_split = []
    for x in range(2):
        temp_nums = []
        temp_suits = []
        for pos in range (5):
            temp_nums.append(convert_list[hand[pos * 2 + shift]])
            temp_suits.append(hand[pos * 2 + shift +  1])
            
        hands_split.append([temp_nums, temp_suits])
        shift += 10
    return (hands_split)

def rank(hand):

    flush = False
    s_h = sorted(hand[0])
    
    # Straight flush
    if hand[1][0] == hand[1][1] == hand[1][2] == hand[1][3] == hand[1][4]:
        flush = True
        if s_h[4]-s_h[3]==1 and s_h[3]-s_h[2]==1 and s_h[2]-s_h[1]==1 and s_h[1]-s_h[0]==1:
            return [9,s_h[4]]
    
    # 4 of a kind
    for x in range(5):
        if s_h[0-x] == s_h[1-x] == s_h[2-x] == s_h[3-x]:
            # print(f'[8,{s_h[0-x]}]')
            return [8,s_h[0-x]]
    
    # Full house
    for x in range(3):
        if s_h.count(s_h[x]) == 3:
            # print(f'found 3 {s_h[x]}')
            f_h = [x for x in s_h]
            f_h.remove(s_h[x])
            f_h.remove(s_h[x])
            f_h.remove(s_h[x])
            if f_h[0] == f_h[1]:
                # print(f'[7,{s_h[x]}] aka Full House w/ {s_h[x]}s and {f_h[0]}s')
                return [7,s_h[x]]
    
    # Flush
    if flush == True:
        return [6,s_h[4],s_h[3],s_h[2],s_h[1],s_h[0]]
    
    # Straight
    if s_h[4]-s_h[3]==1 and s_h[3]-s_h[2]==1 and s_h[2]-s_h[1]==1 and s_h[1]-s_h[0]==1:
        return [5,s_h[4]]
        # print(f'[5,{s_h[4]}]')
    
    # 3 of a kind
    for x in range(3):
        if s_h.count(s_h[x]) == 3:
            # print(f'[4,{s_h[x]}] aka three of a kind w {s_h[x]}s')
            return [4,s_h[x]]
    
    # 2 pairs
    for x in range(4):
        if s_h.count(s_h[x]) == 2:
            p_1 = s_h[x]
            f_h = [x for x in s_h]
            f_h.remove(s_h[x])
            f_h.remove(s_h[x])
            for y in range(2):
                if f_h.count(f_h[y]) == 2:
                    p_2 = f_h[y]
                    f_h.remove(f_h[y])
                    f_h.remove(f_h[y])
                    return [3,max(p_1,p_2),min(p_1,p_2),f_h[0]]
                    # print(f'[3,{max(p_1,p_2)},{min(p_1,p_2)},{f_h[0]}]')  
    
    # Pair
    for x in range(4):
        if s_h.count(s_h[x]) == 2:
            f_h = [x for x in s_h]
            f_h.remove(s_h[x])
            f_h.remove(s_h[x])
            return [2,s_h[x],f_h[2],f_h[1],f_h[0]]
            # print(f'[2,{s_h[x]},{f_h[2]},{f_h[1]},{f_h[0]}]')     

    # High card
    else:
        return [1,s_h[4],s_h[3],s_h[2],s_h[1],s_h[0]]

# hand = [[[5, 5, 6, 7, 13], ['H', 'C', 'S', 'S', 'D']], [[2, 3, 8, 8, 10], ['C', 'S', 'S', 'D', 'D']]]

def who_won(hand):

    hand_1_rank = rank(hand[0])
    hand_2_rank = rank(hand[1])
    
    # print(f'hand_1_rank is {hand_1_rank}; hand_2_rank is {hand_2_rank}')
    
    for y in range(6):
        if hand_1_rank[y] == hand_2_rank[y]:
            continue
        elif hand_1_rank[y] > hand_2_rank[y]:
            # print('True')
            return True
        else:
            # print('False')
            return False

        
f = open("p054_poker.txt", "r")
hand_list = []

for x in range(1000):
    line_temp = f.readline()
    line_str = ''
    count = 1
    for x in range(29):
        if count % 3 != 0:
            line_str += line_temp[x]
        count +=1
    split_hand = split(line_str)
    hand_list.append(split_hand)

player_1_wins = 0
player_2_wins = 0
for hand in hand_list:
    if who_won(hand):
        player_1_wins += 1
    else:
        player_2_wins += 1

print(f'Player 1 won {player_1_wins} out of {player_1_wins + player_2_wins} hands.')
