
import random as rm
import copy

class helper: 

# basic helper functions

	def randomGen():
		a = rm.randint(0,24)
		b = rm.randint(0,24)
		return a, b

	def swapMel(a,b,mel):
		mel[a:b + 1] = mel[a:b + 1][::-1]
		return mel



# mutators

	def mutateRandom(mel):
		melTemp = copy.copy(mel)
		a, b = helper.randomGen()

		if a > b:
			b, a = a, b

		melTemp = helper.swapMel(a,b, melTemp)
		return melTemp





	