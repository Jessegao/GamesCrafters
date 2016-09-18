#Jesse Gao

#game functions
def initial_position():
	return 4
def primitive(pos):
	if pos == 0:
		return 'LOSE'
	elif pos == 1 or pos == 2:
		return "WIN"
	else:
		return 'UNDECIDED'
def gen_moves(pos):
	if pos > 1:
		return [1, 2]
	elif pos == 1:
		return [1]
	else:
		return []
def do_moves(pos, move):
	return pos - m

#memoization
memoization = {2:'WIN', 1:'WIN', 0:'LOSE'}
#can you force a win
def solve(position = initial_position(), isEnemysTurn = False):
	moves = gen_moves(position)
	#print(isEnemysTurn)
	if primitive(position) == 'UNDECIDED':
		if position in memoization and not isEnemysTurn:
			return memoization[position];
		for m in moves:
			if solve(do_moves(m), not isEnemysTurn) == 'LOSE':
				if not isEnemysTurn:
					memoization[position] = 'WIN'
				return 'WIN'
			else:
				if not isEnemysTurn:
					memoization[position] = 'LOSE'
				return 'LOSE'
	else:
		if not isEnemysTurn:
			memoization[position] = 'LOSE'
		return 'LOSE'


#actually not needed, thought i had to write a gametree
class GameTree():

	def __init__(self, position, isEnemysTurn):
		self.position = position
		self.branches = []
		self.isEnemysTurn = isEnemysTurn

	def generateBranches(moves):
		self.branches = [do_moves(position, move) for move in moves]

	def isLeaf(gametree):
		return len(gametree.branches) == 0

