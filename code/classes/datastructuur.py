class data:
	mel = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
	mir = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
	swaps = 0

class node:
	def __init__(self):
		self.swapMel = []
		self.swaps = 0
		self.score = 0
		self.best = False
		self.next = None

	def getScore(self):
		return self.score

	def getNextNode(self):
		return self.next

	def updateScore(self, score):
		self.score = score

	def setNext(self, node):
		self.next = node


class linkedList:
	def __init__(self):
		self.currNode = None

	def addNode(self, swapMel, score, swaps):
		newNode = node()
		newNode.swapMel = swapMel
		newNode.swaps = swaps
		newNode.score = score
		newNode.next = self.currNode
		self.currNode = newNode

	def listPrint(self):
		node = self.currNode
		while node:
			print("Swaps: ", + node.swaps, node.swapMel, " Score:", + node.score)
			# print("Swaps: x", node.swapMel, " Score:", + node.score)

			node = node.next

	# def Max(self):
	# 	start = self.currNode
	# 	maxScore = start.getScore()
	# 	while start:
	# 		if maxScore < start.getScore():
	# 			maxScore = start.getScore()
	# 			node = start
	# 		start = start.next
	# 		# getNextNode()
	# 	return maxScore, node
	#
	# def reverse(self):
	# 	prev = None
	# 	node = self.currNode
	# 	next = node.getNextNode()
	#
	# 	while node:
	# 		node.setNext(prev)
	#
	# 		prev = node
	# 		node = next
	# 		if next:
	# 			next = next.getNextNode()
	# 	self.currNode = prev
