import sys

with open(sys.argv[1], 'r') as f:
	lines = [x.strip() for x in f.readlines()]
	for i in range(0, len(lines)-2, 3):
		print("%s <SEP> %s" % (lines[i+1], lines[i]))
