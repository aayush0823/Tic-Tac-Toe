from copy import deepcopy
import random
from sys import maxsize
import sys
import traceback
from time import time
class bot:
    def __init__(self):
        self.pos_weight = ((4,6,4),(6,3,6),(4,6,4)) # weight of winning position[i][j]
        self.startTime = 0
        self.timeLimit = 23.5
        self.is_bonus = 0
        self.Util_Matrix = [[1,0,0,0],[3,0,0,0],[9,0,0,0],[27,0,0,0]]
        self.boardHash = long(0)
        self.blockHash = [[long(0) for j in xrange(4)] for i in xrange(4)]
        self.blockpoint = 27;

    def move(self, board, old_move, flag):

		if old_move == (-1,-1):
			signal.alarm(0)
			self.addMovetoHash((0,4,4),1)
			return (0,4,4)
		else:
			if board.board_status[old_move[0]][old_move[1]] == self.oppFlag(flag):
				self.addMovetoHash(old_move,0)

		self.who = flag

		maxDepth = 3

		validCells = board.find_valid_move_cells(old_move)
		bestMove = validCells[0]

		try:
			while True:
				self.boardHashSafeCopy = self.boardHash
				self.blockHashSafeCopy = deepcopy(self.blockHash)
				b = deepcopy(board)
				move = self.minimax(b,flag,0,maxDepth,float("-inf"),float("inf"),old_move)[1]
				bestMove = move
				maxDepth += 1
				del b

		except Exception as e:
			self.boardHash = self.boardHashSafeCopy
			self.blockHash = deepcopy(self.blockHashSafeCopy)
			pass

		self.addMovetoHash(bestMove,1)

		return bestMove