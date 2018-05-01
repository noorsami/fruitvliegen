import copy
from helper import *

# Mutators

class mutate:

	def random(mel):
		melTemp = copy.copy(mel)
		a, b = helper.randomGen()

		if a > b:
			b, a = a, b

		melTemp = helper.swapMel(a,b, melTemp)
		return melTemp

