import copy

# listGenerators
class listGen:
	
	# generates x arrays with copys of mel
	def genX(mel, int):
		mel_len = len(mel)
		list = []

		for i in range(int):
			melTemp = copy.copy(mel)
			list.append(melTemp)

		return list;

	# generates x arrays with random mutations from mel
	def genRandom(mel, int):

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