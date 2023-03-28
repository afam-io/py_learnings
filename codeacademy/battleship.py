from random import randint
'''Challenge:
 build a simplified, one-player version of the classic board game Battleship! 
 In this version of the game, there will be a single ship hidden in a random location on a 5x5 grid. 
 The player will have 10 guesses to try to sink the ship.
'''


board = []

# Creates list of lists of 5 rows with 'O' which is the game board
for i in range(5):
   board.append(["O"] * 5)

# Prints board in a grid format with each row on its own line shown as a string
def print_board(board_in):
  for row in board:
    print (" ".join(row))

print_board(board)

# Randomly generates a row and column for the ship
def random_row(board_in):
  return randint(0, len(board_in) - 1)
def random_col(board_in):
  return randint(0, len(board_in) - 1)

# Assigns the ship to a random row and column
ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
  print ("Turn", turn + 1)
  # Print (turn + 1) here!

  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))


  # Checks if the guess is correct
  if guess_row == ship_row and guess_col == ship_col:
    print ("Congratulations! You sunk my battleship!")
    break
  elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print ("Oops, that's not even in the ocean.")
    else:
        print ("You missed my battleship!")
    board[guess_row][guess_col] = "X"
  if turn == 3:
    print ("Game Over")
    print_board(board)
