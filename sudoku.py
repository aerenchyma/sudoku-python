

BOARD_N = 3
BOARD_SIZE = BOARD_N * BOARD_N
# colors later -- Tkinter??

class Board(object):
	def __init__(self, filename):
		self.filename = filename
		self.boardfile = open(filename, 'r')
		self.board,self.orig = self.load_board() # self.board is the changeable one
		self.prevmoves = [] # list of tuples (row, col, valfrom, valto)
	
	def __str__(self):
		s = ''
		for l in self.board:
			s += str(l)+'\n'
		return s
	
	def load_board(self):
		s = self.boardfile.read()
		lines = s.split('\n')
		board = [[int(x) if x.isalnum() else 0 for x in line[:9]] for line in lines] # regex for space?
		orig_spots = [[bool(x) for x in line] for line in board] # unchanging array
		return board, orig_spots
	
	def make_move(self,row,column,value):
		if self.orig[row][column]:
			#print self.orig
			print "not valid -- ln 31"
			return False
		if self.valid_move(value, (row,column)):
			print "checking ln 36"
			origval = self.board[row][column] # saving what it was
			self.prevmoves.append((row, column, origval, value))
			self.board[row][column] = value
			return True
		return False
	 
	def valid_move(self, value, rowcol):
		print "entering valid move"
		#from pudb import set_trace; set_trace()
		row, col = rowcol
		print 'changing to ',value, 'at', rowcol
		if value == 0:
			print "checking 47"
			return True
		if value in self.board[row]:
			return False
		if value in [self.board[x][col] for x in range(BOARD_SIZE)]:
			return False
		top = (row//3) * 3 # integer division of row//3, mult by 3 to find top row of minisquare
		left = (col//3) * 3 # same deal
		indices = [(r,c) for r in range(top,top+3) for c in range(left,left+3)]
		vals = [self.board[r][c] for (r,c) in indices]
		if value in vals:
			return False
		return True

	def check_win(self):
		if any(0 in row for row in self.board):
			return False
		return True

# test fxns

def solver(board):
	nb = solve(0,0, board)
	print nb
	print board

def solve(r,c, board):
		# this needs to check whether permanent
	#if board.orig[r][c]:
	for n in range(1,10):
		print 'trying', n, 'at', r, c
		if board.make_move(r,c,n):
			if c == 8: # this should be its own fxn
				nc = 0
				nr = r + 1
				if nr == 9:
					print "Congratulatory message"
					return True
			else:
				nc = c + 1
				nr = r
			x = solve(nr,nc,board)
			if x:
				return True
	return False
				


def test():
	newboard = Board("sudoku_board_1.txt")
	completeboard = Board("board_full.txt")
	print newboard

	assert newboard.make_move(0,0,6)
	assert not newboard.make_move(0,0,1)
	
	assert newboard.board[0][0] == 6
	
	assert newboard.make_move(1,4,6)
	
	assert newboard.make_move(0,0,0)
	
	assert completeboard.check_win()
	
	


# tests

if __name__ == "__main__":
	
#	test()
	
	testsolve = Board("sudoku_board_1.txt")
	solver(testsolve)