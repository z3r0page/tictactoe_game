#!/usr/bin/python
'''
This is a two player Tic Tac Toe game.
'''
__author__ = 'Amar Sarvepalli'
__email__ = 'errrlog@gmail.com'

import re
import os

def drawGrid(a):
	num = len(a)
	for x in range(num):
		for j in range(num):
			print ' ---',
		print ''
		for k in range(num):
			#print '|   ',
			print '|',  a[x][k],  '',
		print '|'
	for x in range(num):
		print ' ---',
	print ''

def initialize_arr(num, a):
	for i in range(num):
		a.append([])
		for j in range(num):
			a[i].append(0)

def check_grid(a):
	l = len(a)
	for i in range(l):
		for j in range(l):
			if a[i][j] == 0:
				return True
	return False

def check_cell(a, x, y):
	if a[x][y] == 0:
		return True
	else:
		return False

def select_cell(a, p):
	# Player 1
	if p == 1:
	    duin = raw_input("Player 1 Select a box: ")
	    x, y = re.split(',', duin)
	    #x, y = re.split(',\s+', duin)
	    if check_cell(a, int(x), int(y)):
	    	a[int(x)][int(y)] = 1
		os.system('clear')
	        drawGrid(a)
		return 2
	    else:
		print "Err: Cell is not empty. ReEnter correct Cell"
		return 1
	if p == 2:
	    duin = raw_input("Player 2 Select a box: ")
	    x, y = re.split(',', duin)
	    #x, y = re.split(',\s+', duin)
	    if check_cell(a, int(x), int(y)):
	    	a[int(x)][int(y)] = 2
		os.system('clear')
	        drawGrid(a)
		return 1
	    else:
		print "Err: Cell is not empty. ReEnter correct Cell"
		return 2	

def parsg_diag(a):
    res = []
    r = True
    c = True
    ld = True
    rd = True
    l = len(a)
    for i in range(l):
	if a[0][0] != a[i][i]:
	    ld = False
	if a[0][-1] != a[i][l - (i + 1)]:
	    rd = False
	for j in range(l):
	    if a[i][0] != a[i][j]:
		r = False
	    if a[0][i] != a[j][i]:
		c = False
	if r:
	    res.append(a[i][0])
	else:
	    r = True
	if c:
	    res.append(a[0][i])
	else:
	    c = True
    if ld:
	res.append(a[0][0])
    if rd:
	res.append(a[0][-1])
    if res:
	return res
    else:
	return False

def process_result(result):
	if result:
	    if len(result) > 1:
		d = {}
		for i in result:
		    if i in d:
			d[i] += 1
		    else:
			d[i] = 1
		m = max(d.values())
		x = [k for k, v in d.items() if v == m]
		if len(x) > 1:
		    print "Its a Draw"
		    print "Player 1: %d lines" % d[1]
		    print "Player 2: %d lines" % d[2]
		else:
		    print "Player %d Wins. Total lines %d" %(x[0],d[x[0]])
	    else:
		print "Player %d Wins. Total lines 1" % result[0]
	else:
	    print "No Lines, No Wins"

def main():
	uin = raw_input("Enter the size of game board: ")
	os.system('clear')

	a = []
	initialize_arr(int(uin), a)

	drawGrid(a)

	ps = 1
	while check_grid(a):
		ps = select_cell(a, ps)
	# a = [[1, 1, 2, 2], [1, 1, 2, 2], [1, 2, 1, 2], [2, 1, 2, 1]]

	result = parsg_diag(a)
	process_result(result)

if __name__ == '__main__':
	main()
