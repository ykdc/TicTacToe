# Tic Tac Toe Game  

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_not_over = True         

winner = None

current_player = "X"


def play_game():
  # Enable var winner access within function
  global winner
  global board
  global game_not_over

  # Display initial board
  display_board()

  # Loop until there's a winner or tie
  while game_not_over:

    # Handle turn of player
    handle_turn(current_player)

    # Check if game ended
    check_if_game_over()
    
    # Switch to other player
    switch_player()

  # If game over, print winner or tie
  if winner == "X" or winner == "O":
    print(winner + " won!")
  elif winner == None:
    print("It's a Tie")
  
  play_again = input("Do you want to play again? [Y/N]")
  winner = None
  if play_again == "Y" or play_again == "y":
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
    game_not_over = True
    play_game()
  else:
    print("Thank you for playing")


def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])
  print("\n")


# Handle turn of one of the players
def handle_turn(player):

  valid_position = False

  print(player + "'s turn.")
  position = input("Choose a position from 1 to 9: ")

  # Check position user chooses is valid_position & open
  while not valid_position:
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1 to 9: ")

    # Cast var position from string to int, subtract 1 for correct one
    position = int(position) - 1

    # Check position is open
    if board[position] == "-":
      valid_position = True
    else:
      print("Already taken. Choose another position.")
  
  # Put X or O on board at position
  board[position] = player
  display_board()


# Game over if win or board full
def check_if_game_over():
  check_for_winner()
  check_if_tie()


def check_for_winner():
  # Enable var winner access within function
  global winner

  # check if anyone won
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()

  # If TRUE then there was a winner
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None
  return


def check_rows():
  # Enable var game_not_over access within function
  global game_not_over;

  # If all three equal and not equal to "-""
  row1 = board[0] == board[1] == board[2] != "-"
  row2 = board[3] == board[4] == board[5] != "-"
  row3 = board[6] == board[7] == board[8] != "-"

  # Ff any row has 3 of same then game ends
  if row1 or row2 or row3:
    game_not_over = False

  # Return winner X or O  
  if row1:
    return board[0]
  elif row2:
    return board[3]
  elif row3:
    return board[6]
  else: 
    return None


def check_columns():
  # Enable var game_not_over access within function
  global game_not_over;

  # Check if same value and not equal to "-""
  column1 = board[0] == board[3] == board[6] != "-"
  column2 = board[1] == board[4] == board[7] != "-"
  column3 = board[2] == board[5] == board[8] != "-"

  # If any column has 3 of same then game ends
  if column1 or column2 or column3:
    game_not_over = False

  # Return winner X or O  
  if column1:
    return board[0]
  elif column2:
    return board[1]
  elif column3:
    return board[2]
  else:
    return None


def check_diagonals():
  # Enable var game_not_over access within function
  global game_not_over;

  # If all three equal and not equal to "-""
  diagonal1 = board[0] == board[4] == board[8] != "-"
  diagonal2 = board[2] == board[4] == board[6] != "-"

  # If either diagonal has 3 of same then game ends
  if diagonal1 or diagonal2:
    game_not_over = False

  # Return winner X or O  
  if diagonal1:
    return board[0]
  elif diagonal2:
    return board[2]
  else:
    return None


def check_if_tie():
  # Enable var game_not_over access within function
  global game_not_over;

  # Check for open positions
  if "-" not in board:
    game_not_over = False
    return True
  else:
    return False


# Swtich plahyer; X's turn or O's turn
def switch_player():
  #Enable var current_player access within function
  global current_player

  # Check which player & switch to other player
  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"
  return


play_game()    




