
import random as rm
import copy

class helper:

	'''
		This class has helper functions which are useable throughout the code
	'''

	def swapMel(a,b,mel):
		# reverses mel[a:b+1] 
		mel[a:b + 1] = mel[a:b + 1][::-1]
		return mel

	def swapped(i,j,mel):
		# reverses mel[j:len(mel)-i]
		if j > i:
			i,j = j,i

		return mel[:j] + mel[j:len(mel) - i + j + 1][::-1] + mel[len(mel)+ j - i + 1:]


	
	def swapAll(mel):
		# returns all possible swaps as tuple

		newMelList = []
		for i in range(len(mel)):
			for j in range(i):
				newMelList.append(tuple(helper.swapped(i,j,mel)))

		return newMelList

	def makeSequence(mel):
		# makes a list of lists out of a list the innerlists consists
		# of numbers which only differ one from its neighbours
	    newMel = []
	    j = 0
	    for i in range(1,len(mel)):
	        if (abs(mel[i] - mel[i - 1]) is not 1):
	            newMel.append(mel[j:i])
	            j = i
	    newMel.append(mel[j:])

	    return newMel

	def sequenceSwap(start,end,melSequence):
		# reverses a sequence of more from makeSequence 

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
		# returns all possible swaps of a melSequence

	    melSequence = copy.copy(melSequence)
	    newMelList = []
	    for i in range(len(melSequence)):
	        selfSwap = melSequence[:i] + [melSequence[i][::-1]] + melSequence[i+1:]

	        newMelList.append(selfSwap)
	        for j in range(i):
	            newMelList.append(helper.sequenceSwap(j,i,melSequence))
	    return newMelList

	def makeList(seq):
		# returns a list instead of a list of lists
		
	    List = []
	    for i in seq:
	        for j in range(len(i)):
	            List.append(i[j])
	    if type(List[0]) is list:
	        helper.makeList(List)
	    return tuple(List)

	def mutate(mel, int, swapList):

		mel_len = len(mel)

		for i in range(int):
			a = rm.randint(0, mel_len - 1)
			b = rm.randint(0, mel_len - 1)
			swappedMel = helper.swapped(a, b, mel)
			swapList.append(tuple(swappedMel))
		return swapList

	# make an ordered tuple combining scoreList with swapList
	def makeTuple(tupleSwap, scoreList, swapList):
		i = 0
		for swap in swapList:
			tupleSwap.append((scoreList[i], swap))
			i+=1
		return tupleSwap

	# function to check is list is reversed
	def isReversed(mel):
		for i in range( len(mel) - 1 ):
			if mel[i] < mel[i+1]:
				return False
			return True

	''' Function for mutating a single mel with random values '''
	def mutateSingle(mel):
	    mel_len = len(mel)
	    a = rm.randint(0, mel_len - 1)
	    b = rm.randint(0, mel_len - 1)
	    swappedMel = helper.swapped(a,b,mel)
	    return swappedMel
