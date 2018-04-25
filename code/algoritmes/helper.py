
import random as rm
import copy

class helper: 
	def randomGen():
		a = rm.randint(0,24)
		b = rm.randint(0,24)
		return a, b

	def swapMel(a,b,mel):
		mel[a:b + 1] = mel[a:b + 1][::-1]
		return mel

	def gen(mel, int):

		mel_len = len(mel)
		swapList = []

		for i in range(int):
			melTemp = copy.copy(mel)
			a = rm.randint(0, mel_len - 1)
			b = rm.randint(0, mel_len - 1)

			if a > b:
				b, a = a, b

			melTemp = helper.swapMel(a,b,melTemp)
			
			swapList.append(melTemp)

		return swapList
	