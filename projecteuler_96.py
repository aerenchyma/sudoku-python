import sudoku

# separate the text file, the silly way
f = open("sudoku_projecteulerboards.txt")
fl = f.read()
fls = fl.split("Grid")
count = 0
objs = []
for item in fls:
	count += 1
	fr = open("peboard%s.txt" % str(count),'w')
	fr.write(item)
	fr.close()
	objs.append("peboard%s.txt" % str(count))
for n in objs:
	name = n
	q = open(n, 'r+')
	lines = q.readlines()
	q.close()
	f = open(name,'w')
	f.write(''.join(lines[1:]).rstrip())
	f.close()

# solve them all and save

# peboards = []
# nums = range(2,52)
# for i in nums:
# 	f = "peboard%s.txt" % str(i)
# 	nb = Board(f)
# 	peboards.append(nb)
# ints = []
# for b in peboards:
# 	s = find_solution(b)
# 	m = int(''.join([str(y) for y in s.board[0][:3]])) 
# 	ints.append(m)		
# print sum(ints)

# answer: 24702
# time on this solution: somewhat more than might be desired (thx lists)
## next: smart solver