# tick_tack_toe
# from Ipython.display import clear_output

# global variables
game_on= True
sign1=""
sign2=""
player1_name=""
player2_name=""
p="" # hold player name value
t=""  # holds players sign value
row=0
column=0
empty = [[" "," "," "],[" "," "," "],[" "," "," "]] # for the sake of clear
container=[[" "," "," "],[" "," "," "],[" "," "," "]]
sign=[]
players=[]

# take players name and sign
def player_data():
    global sign1
    global sign2
    global player1_name
    global player2_name
    print(" player 1 :\n")
    player1_name = input("Enter your name :")
    sign1= input(" prefered sign1: ")
    players.append(player1_name)
    sign.append(sign1)
    print(" player 2 :\n")
    player2_name = input(" Enter your name :")
    sign2= input(" prefered sign2: ")
    players.append(player2_name)
    sign.append(sign2)

#  change the turn of the players
# flip the turn for known signes by reverse logic
def flip():
    global p
    global t
   
    sign.reverse()
    players.reverse()
    t=sign[0]
    p=players[1]
    return t


    
    

# the matrics
def display_matrix():
    print(f"{container[0][0]} |{container[0][1]} |{container[0][2]}") # row
    print("- - - - - ")
    print(f"{container[1][0]} |{container[1][1]} |{container[1][2]}") #row2
    print("- - - - - ")
    print(f"{container[2][0]} |{container[2][1]} |{container[2][2]}")# row 3


# __ check if there is space___
# return boolian by comparing with empty space
def is_there_space(rw,col):
    return container[rw][col]==" "
#  ___check if full board is taken
def is_the_full_board_taken():
    for rw in range(3):
        for col in range(3):
            if is_there_space(rw,col): # if there is space it is not full
                return False
    return True


#  ____choose index_________
#  check proper index number(1-9) is selected and the selected index is not taken
#  otherwise ask the user again until it select proper index

def insert_at():
    index=0
    global row
    global column
    while(index not in[1,2,3,4,5,6,7,8,9]or not is_there_space(row,column)): 
        try:
            index= int(input("please select free index :"))
        except:
            print("please enter intiger format only 1 - 9")
            
        if index==1:
            row = 0
            column =0
        elif index == 2:
            row= 0
            column=1
        elif index == 3:
            row= 0
            column=2
        elif index == 4:
            row= 1
            column=0
        elif index == 5:
            row= 1
            column=1
        elif index == 6:
            row= 1
            column=2
        elif index == 7:
            row= 2
            column=0
        elif index == 8:
            row= 2
            column=1
        elif index == 9:
            row= 2
            column=2
    container[row][column]=flip()  # assign the sign of the player at specified index

# _______________check WIN_______________
def check_answer():
    global game_on

    if ( container[0][0]==container[0][1]==container[0][2]==t or # row 1
         container[1][0]==container[1][1]==container[1][2]==t or# row 2
         container[2][0]==container[2][1]==container[2][2]==t): # row 3
        nop=flip()
        print(f" player {p} WIN")
        game_on=False
        return 0
    elif (container[0][0]==container[1][0]==container[2][0] ==t or #columun 1
           container[0][1]==container[1][1]==container[2][1]==t or  #columun 2
            container[0][2]==container[1][2]==container[2][2]==t ):  #columun 3
        nop=flip()
        print(f" player {p} WIN")
        game_on=False
        return 0
    elif ( container[0][0]==container[1][1]==container[2][2]==t or #diagonal
         container[0][2]==container[1][1]==container[2][0]==t ): 
        nop=flip()
        print(f" player {p} WIN")
        game_on=False
        return 0  # stop ieration
    else:
        return  # continue iteration as it is

# _______clear_______
# put empty space for each index
def clear():
    for rw in range(3):
        for col in range(3):
            container[rw][col]=' ' #clear
    print("\n"*30)  #creat many new line     

# __________-replay_________
# prompt to play again 
# if y clear and recurse the game function
# if no break and print BYE!
def replay():
    play = input("do you wanna play tik tak toe again ? y or n ")
    if play=="y":
        return True 
    else:
        return False

def game():
    global game_on
    global row
    global column
    display_matrix() # empity matrix

    full=False
    while(not full):
        # print(f"{row} {column}")
        print(f"{p} turn ")

        insert_at()
        display_matrix()
        win = check_answer() # return 0 if there is a winner
        if win==0:
            break
        else:
            full=is_the_full_board_taken()
            if full:
                print("the game is tie")
                print("no winner \n")
                game_on=False        
            else:
                game_on=True
      
    
player_data()
while(1):
    player= flip() # flip to choose first player
    print(f" first round player is {p}")

    
    game_on=True

    while(game_on):
        game()
    
    cont=replay() # check to continue or exit
    if cont:
        clear()
    else:
        print("\n\n BYE! come again")
        break



