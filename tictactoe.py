#------------Global Variables-----------

# game board
board = ["-", "-", "-", 
         "-", "-", "-",
         "-", "-", "-"]

# if game still going
game_still_going = True

# who won or tie    
winner = None

# whos turn is it    
current_player = "x"

# display board
def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])

# play game
def play_game():
  # display initial board
  display_board()
  
  #loop through turn
  while game_still_going:

    #handle player turn
    handle_turn(current_player)

    #check game still on
    check_if_game_over()

    # change player if game not over
    flip_player() 
  
  #game has ended
  if winner == "x" or winner == "o":
    print(winner + " won.")
  elif winner == None:
    print('Tie.')

def handle_turn(player):
  
  print(player +"'s turn.")
  position = input("Choose a position from 1-9: ")

  # loop user can not key in if board already field.
  valid = False
  while not valid:

    # ask user to key in again of insert value outside of 1-9
    while position not in ["1", "2", "3", "4","5","6","7","8","9"]:
      position = input("Invalid input. Choose a position from 1-9: ")

    #get the correct index for the board list
    position = int(position) - 1 

    #if board already fielded, user need to enter again.
    if board[position] == "-":
      valid = True
    else:
      print("You can't enter here. Go again.")

  board[position] = player
  display_board()

def check_if_game_over():
  check_for_winner()
  check_if_tie()

def check_for_winner():
  #setup global variable. now we can change the value of this global variable
  global winner

  # check row
  row_winner = check_rows()
  # check column 
  column_winner = check_column()
  # check diagonals
  diagonal_winner = check_diagonal()
  if row_winner:
    #there was a winner
    winner = row_winner
  elif column_winner:
    #there was a winner
    winner = column_winner
  elif diagonal_winner:
    #there was a winner
    winner = diagonal_winner
  else:
    #there was no winner
    winner = None
  return

def check_rows():

  global game_still_going

  #boolean. check if row have the same value and not -
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"

  # if any row match true, flag there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False
  
  #return winner x or 0
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return
  
def check_column():

  global game_still_going

  #boolean. check if column have the same value and not -
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"

  # if any column match true, flag there is a win
  if column_1 or column_2 or column_3:
    game_still_going = False
  
  #return winner x or 0
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  return

def check_diagonal():

  global game_still_going

  #boolean. check if diagonal have the same value and not -
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[6] == board[4] == board[2] != "-"
  
  # if any column match true, flag there is a win
  if diagonal_1 or diagonal_2:
    game_still_going = False
  
  #return winner x or 0
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[6]
  return
  
def check_if_tie():
  global game_still_going

  if "-" not in board:
    game_still_going = False
  return

def flip_player():

  global current_player

  # == check if current player EQUAL to x, change to o
  if current_player == "x":
    current_player = "o"
  # == check if current player EQUAL to o, change to x
  elif current_player == "o":
    current_player = "x"
  return

play_game()



