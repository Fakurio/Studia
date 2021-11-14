from random import randint

board = [[1,2,3],[4,5,6],[7,8,9]]

def display_board():
    print("+","-"*7,"+","-"*7,"+","-"*7,"+")
    print("|"," "*7,"|"," "*7,"|"," "*7,"|")
    print("|"," "*2,board[0][0]," "*2,"|"," "*2,board[0][1]," "*2,"|"," "*2,board[0][2]," "*2,"|")
    print("|"," "*7,"|"," "*7,"|"," "*7,"|")
    print("+","-"*7,"+","-"*7,"+","-"*7,"+")
    print("|"," "*7,"|"," "*7,"|"," "*7,"|")
    print("|"," "*2,board[1][0]," "*2,"|"," "*2,board[1][1]," "*2,"|"," "*2,board[1][2]," "*2,"|")
    print("|"," "*7,"|"," "*7,"|"," "*7,"|")
    print("+","-"*7,"+","-"*7,"+","-"*7,"+")
    print("|"," "*7,"|"," "*7,"|"," "*7,"|")
    print("|"," "*2,board[2][0]," "*2,"|"," "*2,board[2][1]," "*2,"|"," "*2,board[2][2]," "*2,"|")
    print("|"," "*7,"|"," "*7,"|"," "*7,"|")
    print("+","-"*7,"+","-"*7,"+","-"*7,"+")

def make_list_of_free_fields():
    free_fields = []
    for i in range(3):
        for j in range(3):
            if board[i][j] in range(1,10):
                free_fields.append((i,j))
    return free_fields

def enter_move():
    free_fields = make_list_of_free_fields()
    if len(free_fields) == 0:
        return 0
    while True:
        flag = False
        field_number = int(input("Select a field to draw a circle ")) 
        for i, j in free_fields:
            if board[i][j] == field_number:
                board[i][j] = "O"
                flag = True
                break

        if flag:
            break
        else:
            print("You have selected a wrong field")

def draw_move():
    if board[1][1] == 5:
        board[1][1] = "X"
    else:
        free_fields = make_list_of_free_fields()
        if len(free_fields) == 0:
            return 0
        while True:
            x = randint(0,2)
            y = randint(0,2)
            if (x,y) in free_fields:
                board[x][y] = "X"
                break

def victory_for(sign):
    flag = False
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == sign:
            flag = True
            break
        elif board[i][0] == board[i][1] == board[i][2] == sign:
            flag = True
            break
        elif (board[0][0] == board[1][1] == board[2][2] == sign) or (board[2][0] == board[1][1] == board[0][2] == sign):
            flag = True
            break
    if flag:
        return True
    return False

def game():
    flag = False
    while len(make_list_of_free_fields())!=0:
        draw_move()
        display_board()
        if victory_for("X"):
            print("Computer wins")
            flag = True
            break
        enter_move()
        display_board()
        if victory_for("O"):
            print("You win")
            flag = True
            break
    if not flag:
        print("Tie")
    
    

game()




