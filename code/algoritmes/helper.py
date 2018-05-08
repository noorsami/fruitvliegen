
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

	def swapped(i,j,mel):
		if j > i:
			i,j = j,i

		return mel[:i] + mel[i:j][::-1] + mel[j:]
