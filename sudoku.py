# SUDOKU

BOARD_N = 3
BOARD_SIZE = BOARD_N * BOARD_N
# colors later

class Board(object):
	def __init__(self, filename):
		self.filename = filename
		self.boardfile = open(filename, 'r')
		self.board,self.orig = self.load_board() # self.board is the changeable one. self.load_board() returns a tuple
		self.prevmoves = [] # list of tuples (row, col, valfrom, valto)
		self.error = None # for keeping track of why a move is invalid
	
	def __str__(self): # TODO: format more clearly
		sp = '  ' 
		s = "  "
		digits = range(1,10)
		s += sp
		for n in digits:
			s += str(n)+ sp
		s += '\n'
		s += sp*2
		for n in digits:
			s += "_" + sp
		s += '\n'
		count = 0 
		#from pudb import set_trace ; set_trace()
		for l in self.board:
			s += str(digits[count]) + " | "
			for item in l:
				s += str(item)+ sp
			s += '\n'
			count += 1
		return s
	
	def load_board(self):
		s = self.boardfile.read()
		lines = s.split('\n')
		board = [[int(x) if x.isalnum() else 0 for x in line[:9]] for line in lines] 
		orig_spots = [[bool(x) for x in line] for line in board] # unchanging array
		return board, orig_spots
	
	def make_move(self,row,column,value):
		if self.orig[row][column]:
			#print self.orig
			return False
		if self.valid_move(value, (row,column)):
			origval = self.board[row][column] # saving what it was
			self.prevmoves.append((row, column, origval, value))
			self.board[row][column] = value
			return True
		return False
	 
	def valid_move(self, value, rowcol):
		row, col = rowcol
		if value == 0:
			return True
		if value in self.board[row]:
			self.error = "Invalid Row"
			return False
		if value in [self.board[x][col] for x in range(BOARD_SIZE)]:
			self.error = "Invalid Column"
			return False
		top = (row//3) * 3 # integer division of row//3, mult by 3 to find top row of minisquare (the 3x3 squares)
		left = (col//3) * 3 # find furthest left, same deal
		indices = [(r,c) for r in range(top,top+BOARD_N) for c in range(left,left+BOARD_N)]
		vals = [self.board[r][c] for (r,c) in indices]
		if value in vals:
			self.error = "Invalid Square"
			return False
		if is_permanent(rowcol[0],rowcol[1], self): 
			self.error = "Not alterable" 
			return False
		return True
		
	def undo(self): # can undo only the last move (currently the undo then becomes the previous move) 
	## poss.TODO: implement continuous undo
	## TODO: can't undo after trying to solve an unsolveable board, which is a problem
		if self.prevmoves != []:
			xr, xc = (self.prevmoves[-1][0], self.prevmoves[-1][1])
			xv = self.prevmoves[-1][2]
			if self.make_move(xr,xc,xv):
				return True
		else:
			print "Sorry, you haven't made any moves yet. Try something else."
			return True
		#self.board[xr][xc] = self.prevmoves[-1][2]
		return False # should never happen
	
	def fix_board_state(self): # for solving-at-state. TODO: adjustments
			for r in range(BOARD_SIZE):
				for c in range(BOARD_SIZE):
					if self.board[r][c]:
						if not self.orig[r][c]: 
							self.orig[r][c] = True

	def check_win(self):
		if any(0 in row for row in self.board):
			return False
		return True

# solver fxns
# (brute force solution)
def solver(board): 
	"""Returns True if solves board, else False"""
	for c in range(BOARD_SIZE):
		for r in range(BOARD_SIZE):
			assert bool(board.orig[r][c]) == bool(board.board[r][c]) 
	# Asserts that every filled-in square is a permanent square
	r, c = 0, 0
	if board.check_win():
		return True
	while is_permanent(r, c, board):
		r, c = get_next(r, c, board)
	nb = solve(r,c,board)
	print board
	return nb

def find_solution(board):
	"""Same as solver, but returns the actual board instance that is solved"""
	# for c in range(BOARD_SIZE):
	# 	for r in range(BOARD_SIZE):
	# 		assert bool(board.orig[r][c]) == bool(board.board[r][c]) 
	# Asserts that every filled-in square is a permanent square
	r, c = 0, 0
	if board.check_win():
		return True
	while is_permanent(r, c, board):
		r, c = get_next(r, c, board)
	nb = solve(r,c,board)
	return board
	
def solve(r,c, board):
	for n in range(1,10):
		if board.make_move(r,c,n):
			if board.check_win():
				return True
			nr, nc = get_next(r, c, board)
			while is_permanent(nr, nc, board):
				nr, nc = get_next(nr, nc, board)
			x = solve(nr,nc,board)
			if x:
				return True
	board.board[r][c] = 0
	return False

def is_permanent(r, c, board):
	return board.orig[r][c]

def is_changeable(r, c, board):
	return not board.orig[r][c]	

def get_next(r,c,board):
	#TODO fix for board size 
	if c == 8:
		nc = 0
		nr = r + 1
		if nr == 9:
			nc, nr = 0,0
	else:
		nc = c + 1
		nr = r
	return nr, nc



def test():
	# creating/loading sudoku boards
	newboard = Board("sudoku_board_1.txt") # to play
	completeboard = Board("board_full.txt") # is a winning board
	print newboard
	newboard.make_move(0,0,7)
	print newboard
	# newboard.undo() ## testing undo
	# print newboard
	
	## assertions
	assert newboard.make_move(0,0,6)
	assert not newboard.make_move(0,0,1)
	assert newboard.board[0][0] == 6
	assert newboard.make_move(1,4,6)
	print newboard
	assert newboard.make_move(0,0,0)
	assert not newboard.check_win()
	assert completeboard.check_win()
	print "All tests pass."
	


# tests

if __name__ == "__main__":
	
	test()
	# testsolve = Board("sudoku_board_1.txt") 
	# solver(testsolve)