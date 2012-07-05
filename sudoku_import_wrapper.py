import sudoku
import sys, os #maybe we'll see

# functions

def print_dirs(): #TODO: remember, x axis and y axis as a user would see it are *c* and *r* respectively, must correct for that (do so in get_coords)
	s = """_________ SUDOKU __________\n
	(P)lace value -- put in format X-coord,Y-coord,Value-to-Place\n
	(T)ry -- to place a value in the board (X-axis, )
	(S)olve game -- solves board at current state\n
	(Q)uit game -- ends game and quits program\n
	(U)ndo last move [TODO]\n
	(H)elp -- prints these directions again\n"""
	return s # so should take from user something that looks like: 1,3,7 where the coord is (1,3) -- (3,1) programatically -- and the val is 7
	
def get_coords(): #TODO: need to correct for the 0/1 off-by-one
# also need to fix the fact that these should not be separate while-loops because it will never work
	c = int(raw_input("Enter an x coordinate (1-9): "))
	r = int(raw_input("Enter a y coordinate (1-9): "))
	v = int(raw_input("Enter a value to place (1-9): "))
	while not c.isnum():
		print "Enter single digit integers.\n"
		c = int(raw_input("Enter an x coordinate (1-9): "))
	while not r.isnum():
		print "Enter single digit integer.\n"
		r = int(raw_input("Enter a y coordinate (1-9): "))
	while not v.isnum():
		print "Enter single digit integer.\n"
		v = int(raw_input("Enter a value to place (1-9): "))
	return r,c,v # playgame will have to use the results of this when you need to get r and c from player

# takes the current board of type Board in sudoku, uses prevmoves record to undo
# undoing: that will append the "undo" move to the prevmoves list, right? so that's now the last move...
def undo(board):
	print "You can only undo the LAST move. Make sure this is what you want to do." #TODO? no way to go back from this point as is
	xr, xc = (board.prevmoves[-1][0],board.prevmoves[-1][1])
	board.board[xr][xc] = board.prevmoves[-1][2] # reassigns that previous move space to the 'valfrom' value (valto should thus be overwritten)
	# more?
	# should I return the board so that it is The Board? that object model is getting lost in all this, I should draw it out.

# takes current board, makes all extant values permanent so the remainder can be solved
# returns board with permanent non-zero entered values + orig perm values, to pass to the sudoku solver
def solve_board_state(board):
	# board.board is a list of lists of numbers
	# want a list of tuples of coords (r,c) where the number is not zero
	places = [(r,c) for board.board[r][c] in board.board if board.board[r][c] is not 0]
	#print places # for testing
	for r,c in places:
		board.orig[r][c] = True
	return board 


def quit():
	return None # how do you quit - A: you just stop running the playgame loop and let it finish, so this is not necessary

def place_value(board):
	r,c,v = get_coords()
	board.make_move(r,c,v)

def solve_game(board):
	permboard = solve_board_state(board)
	return solver(permboard) # this will print within the solving function now, so no need for print command here

def print_board(board):
	print board

		
def play_game():
	command = raw_input(print_dirs())
	return command


# main fxn loop
def main():
	command = play_game()
	while command != 'Q':
		# want to print the board somewhere... look at where it is being printed -- take out the check in the class
		# when does a class instance get created?
		command = play_game()
	return None

if __name__ == "__main__":

	main()