import sudoku

# PROBLEMS:
# p /-> 1,9,3 --> "did you forget to enter something"
# occasional 1-9 inclusive errors when shouldn't be
# no indication of when not a valid move and why not
# should have a command to view the board

## this problem, on a move that should be valid:
# """Enter x-coord, y-coord, value to place, separated by commas..
# E.g. 2,3,7.
# 1,9,3
# Did you forget to enter something?
# 
# Enter x-coord, y-coord, value to place, separated by commas..
# E.g. 2,3,7.
# 1,1,9
# Traceback (most recent call last):
#   File "sudoku_import_wrapper.py", line 86, in <module>
#     while command != 'Q':
#   File "sudoku_import_wrapper.py", line 77, in main
#     return board # having been changed in fxn
#   File "sudoku_import_wrapper.py", line 56, in play_game
#     def play_game(board, command):
#   File "sudoku_import_wrapper.py", line 34, in get_coords
#     try:
# UnboundLocalError: local variable 'r' referenced before assignment
# """

# unclear whether it's looping to 'place a value' or 'put in a command and then do a thing if needed' 
# --> that's also an 'interface' decision (better to have it assume place a value and then take a command if it's something else?)

# first entering of 'p' as stands does not bring you to "enter coords/val" prompt, just prints the board

# functions

def print_dirs(): #TODO: remember, x axis and y axis as a user would see it are *c* and *r* respectively, must correct for that (do so in get_coords)
	s = """_________ SUDOKU __________\n
	(P)lace value -- put in format: X-coord,Y-coord,Value-to-Place\n
	(U)ndo last move (can ONLY undo the immediately previous move)\n
	(S)olve game -- solves board at current state\n
	(Q)uit game -- ends game and quits program\n
	(H)elp -- prints these directions again\n"""
	return s # so should take from user something that looks like: 1,3,7 where the coord is (1,3) -- (3,1) programatically -- and the val is 7
	
def get_coords(): #TODO: need to correct for the 0/1 off-by-one
# also need to fix the fact that these should not be separate while-loops because it will never work
	placeval = raw_input("Enter x-coord, y-coord, value to place, separated by commas..\nE.g. 2,3,7.\n")
	nums = placeval.split(",")
	usefuln = []
	try:
		for item in nums:
			item = item.strip() # gets rid of extra spaces around columns
			usefuln.append(int(item))
	except:
		print "Please enter integers separated by commas.\n"
		get_coords()
	try:
		r,c,v = usefuln[1]-1,usefuln[0]-1,usefuln[2] # correcting for the y vs x deal and the off-by-one
	except:
		print "Did you forget to enter something?\n"
		get_coords()	
	if any(i < 1 or i > 9 for i in usefuln):
		print "Integers should be 1-9 inclusive.\n"
		return get_coords() # if it's an invalid number for place or value, try again and return those values
	return r,c,v

def place_value(board):
	r,c,v = get_coords()
	board.make_move(r,c,v)

def solve_game(board):
	#permboard = board.fix_board_state() ## method needs fixing
	return solver(permboard) # this will print within the solving function now, so no need for print command here

def print_board(board):
	print board

		
def play_game(board, command):

	print board
	while not board.check_win():
		command = raw_input(print_dirs()).upper()
		print board 
		print "just tried", command
		if command == 'P':
			r,c,v = get_coords()
			board.make_move(r,c,v)
		
		elif command == 'U':
			board.undo()
		elif command == 'S':
			#	board.fix_board_state()
				
				if not sudoku.solver(board):
					print "This board is unsolveable. Try again!" # unsolveable at current state.
					##TODO: option for solving originally-given board
				else: solve_game(board)
		elif command == 'Q':
			pass
		#print board
	return board # having been changed in fxn


# main fxn loop
def main():
	print "Welcome to Sudoku.\n"
	game_board = sudoku.Board("sudoku_board_1.txt")
	command = raw_input(print_dirs()).upper()
	play_game(game_board,command)
	while command != 'Q':
		game_board = play_game(game_board,command)
	return None
		
	

if __name__ == "__main__":

	main()