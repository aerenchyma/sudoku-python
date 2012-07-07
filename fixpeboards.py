import re

f = open("sudoku_projecteulerboards.txt")
fl = f.read()
# the silly non-re way
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
	# write the same file without the first line
	lines = q.readlines()
	q.close()
	
	f = open(name,'w')
	f.write(''.join(lines[1:]))
	f.close()