from random import randint, choice

lines=["012","345","678","036","147","258","048","246"]

p1_moves_in_lines={"012":0,
                    "345":0,
                    "678":0,
                    "036":0,
                    "147":0,
                    "258":0,
                    "048":0,
                    "246":0
                    }

p2_moves_in_lines={"012":0,
                    "345":0,
                    "678":0,
                    "036":0,
                    "147":0,
                    "258":0,
                    "048":0,
                    "246":0
                    }

p1_moves = []
p2_moves = []

next_move = None

def next_possible_move():
    sort_orders = sorted(p2_moves_in_lines.items(), key=lambda x: x[1], reverse=True)
    max_count=0
    possible_lines=[]
    for i in sort_orders:
        if i[1]>max_count:
            max_count=i[1]
            possible_lines.append(i[0])
        if i[1]==max_count and (i[0] not in possible_lines):
            possible_lines.append(i[0])

    possible_moves=[]
    if len(possible_lines)==0:
        while True:
            move = str(randint(0,8))
            if  (move in p1_moves or move in p2_moves)==False:
                return move

    for line in possible_lines:
        for move in line:
            if (move in p1_moves or move in p2_moves or move in possible_moves) == False:
                possible_moves.append(move)
    
    if len(possible_moves)==0:
        while True:
            move = str(randint(0,8))
            if  (move in p1_moves or move in p2_moves)==False:                return move
    
    print("Possible Moves:", possible_moves)
    while True:
        move = choice(possible_moves)
        if (move in p1_moves or move in p2_moves)==False:
            return move

def wincheck(player_moves, current_move):
    for line in lines:
        if current_move in line:
            moves_in_line=0
            for a_move_in_line in line:
                if a_move_in_line in player_moves or a_move_in_line==current_move:
                    moves_in_line+=1
            if moves_in_line>2:
                print("Player Winning Move:", current_move)
                print("Player wins", line)
                return current_move
    return None

while True:
    p1_move = input("Player 1: ")
    p1_moves.append(p1_move)
    
    if len(p1_moves+p2_moves)==9:
        print("Match Draw")
        break

    if wincheck(p1_moves, p1_move) !=None:
        break

    next_move_2 = None

    for line in lines:
        if p1_move in line:
            p1_moves_in_lines[line]+=1
            if p1_moves_in_lines[line]==2:
                for move in line:
                    if not (move in p1_moves or move in p2_moves):
                        next_move_2=move
    
    next_move=str(next_possible_move())
    jitse = wincheck(p2_moves,next_move)
    if jitse != None: break
    if jitse==None and next_move_2 != None and next_move not in p1_moves:
        next_move=next_move_2
    
    p2_move = next_move
    p2_moves.append(next_move)
    for line in lines:
        if p2_move in line:
            p2_moves_in_lines[line]+=1

    print("Player 2:", p2_move)
    print("P1 Moves")
    print(p1_moves_in_lines)
    print("P2 Moves")
    print(p2_moves_in_lines)


