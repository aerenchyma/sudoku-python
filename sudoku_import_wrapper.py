# command line interface for sudoku
# Jackie Cohen

import sudoku

# functions

def print_dirs(): 
	s = """_________ SUDOKU __________\n
	(P)lay Game\n
	(U)ndo last move (can ONLY undo the immediately previous move)\n
	(S)olve game -- solves board at current state\n"""
	return s  #TODO: add help and quit
	
def get_coords(): 
	placeval = raw_input("Enter x-coord, y-coord, value to place, separated by commas..\nE.g. 2,3,7.\n")
	if placeval.upper() == 'S':
		return None # check
	elif placeval.upper() == 'U':
		return '0' # another check -- STRING 0
	elif placeval.upper() == 'Q':
		return '1'
	elif len(placeval.split(",")) == 3:
		nums = placeval.split(",")
		usefuln = []
		try:
			for item in nums:
				item = item.strip() # gets rid of extra spaces around columns
				usefuln.append(int(item))
		except:
			print "Please enter integers separated by commas.\n"
			get_coords()
		# try:
		r,c,v = usefuln[1]-1,usefuln[0]-1,usefuln[2] # correcting for the y vs x and the off-by-one
		if any(i < 1 or i > 9 for i in usefuln):
			print "Integers should be 1-9 inclusive.\n"
			return get_coords() # if it's an invalid number for place or value, try again and return those values
		return r,c,v
	else:
		print "There was an error. Try again. \n"
		return get_coords() # if you enter anything unexpected, prompts you again

def place_value(board):
	r,c,v = get_coords()
	board.make_move(r,c,v)

def print_board(board):
	print board
		
def play_game(board, command):

	print board
	while not board.check_win():
		print_dirs()
		rcv_tuple = get_coords()
		if rcv_tuple == None: 
			board.fix_board_state()
			if sudoku.solver(board):
					print "Congratulatory message"
			else:
				print "This board is unsolveable. Try again!" # unsolveable at current state.
		elif rcv_tuple == '0':
				board.undo()
		elif rcv_tuple == '1': # TODO: fix haaaaackyness
			break
		else:
			if not board.make_move(*rcv_tuple):
				print board.error
			print board
	return board # having been changed in fxn


# main fxn loop
def main():
	print "Welcome to Sudoku.\n"
	game_board = sudoku.Board("sudoku_board_1.txt")
	command = raw_input(print_dirs()).upper()
	play_game(game_board,command)
	while not game_board.check_win():
		print game_board
		game_board = play_game(game_board,command)
	return None
		
	

if __name__ == "__main__":

	main()