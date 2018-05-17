
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

		return mel[:j] + mel[j:len(mel) - i + j + 1][::-1] + mel[len(mel)+ j - i + 1:]


	# returns all possible swaps
	def swapAll(mel):
		newMelList = []
		for i in range(len(mel)):
			for j in range(i):
				newMelList.append(tuple(helper.swapped(i,j,mel)))

	return newMelList

	# checks a list for dublicates and returns a list of lists
	def noDublicates(list):
		listSet = set(tuple(item) for item in list)
		noDublicate = []
		for item in listSet:
			noDublicate.append(item)
		return noDublicate

	def makeSequence(mel):
		newMel = []
		j = 0
		for i in range(1,len(mel)):
			if (abs(mel[i] - mel[i - 1]) is not 1):
				newMel.append(mel[j:i])
				j = i
			newMel.append(mel[j:])
		return newMel

	def sequenceSwap(start,end,melSequence):
		if start > end:
			start, end = end, start

		melSequence = copy.copy(melSequence)
		newMelSequence = melSequence[:start]
		check = 0

		if end is len(melSequence) - 1:
			newMelSequence.extend([melSequence[end][::-1]])
			end -= 1
			check +=1

		for i in range(end - start + 1):
			newMelSequence.append(melSequence[end - i][::-1])

		if not check:
			newMelSequence.extend(melSequence[end + 1:])

		return newMelSequence

	def swapAllSequence(melSequence):
		melSequence = copy.copy(melSequence)
		newMelList = []
		for i in range(len(melSequence)):
			selfSwap = melSequence[:i] + [melSequence[i][::-1]] + melSequence[i+1:]
			newMelList.append(selfSwap)
			for j in range(i):
				newMelList.append(sequenceSwap(j,i,melSequence))

		return newMelList

	def makeList(seq):
		List = []
		for i in seq:
			for j in range(len(i)):
				List.append(i[j])
		if type(List[0]) is list:
			makeList(List)
		return tuple(List)