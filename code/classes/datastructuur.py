class data:
	mel = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
	mir = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
	swap = 0

class node:
	def __init__(self):
		self.swapMel = []


		self.history = []
		self.score = 0



		self.next = None

class linkedList:
	def __init__(self):
		self.currNode = None

	def addNode(self, swapMel):
		newNode = node()
		newNode.swapMel = swapMel
		newNode.next = self.currNode
		self.currNode = newNode

	def listPrint(self):
		node = self.currNode
		while node:
			print(node.swapMel)
			node = node.next
