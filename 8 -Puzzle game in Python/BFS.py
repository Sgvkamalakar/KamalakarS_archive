#from time import clock
from collections import deque
from State import State
from Solver import Solver
goalTest = [[1,2,3],[8,0,4],[7,6,5]]

class BFS(Solver):

	def solve(self):
		self.expandedNodes += 1
		before = clock()
		frontier = deque([self.initialState])
		self.explored.add(self.initialState.id)
		while frontier:
			state = frontier.popleft()
			state.getFManhattan()
			if (state.board == goalTest):
				self.finalState = state
				self.runningTime = clock() - before
				return True
			if state.depth+1 > self.depth:
				self.depth = state.depth+1
			for neighbor in state.neighbors():
				if not ((neighbor.id in self.explored)):
					self.explored.add(neighbor.id)
					frontier.append(neighbor)
		self.runningTime = clock() - before
		return False

