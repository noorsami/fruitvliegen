from helper import helper
import time
import matplotlib.pyplot as plt

''' Pancake sorting algorithm. '''
def pancakeSort(mel, mir):
	'''
	Pancake sorting is a informal term for the mathematical problem of sorting a
	disordered stack of pancakes in order of size when a spatula can be
	inserted at any point in the stack and used to flip all pancakes above it.
	It is a variation of the sorting problem in which the only allowed operation
	is to reverse the elements of some prefix of the sequence.

	This is also the case with the Drosophila-case. Instead of pancakes of
	different sizes, this algorithm sorts genome-sequences based on the appended
	values to each genome. The highest valued-genome (Alk, value: 25) is the
	figurative largest pancake that needs to end up on the bottom of the stack.
	The lowest valued-genome (cos, value: 1) is the equivalent of the smallest
	pancake and needs to end up on top of the stack.

	              Arguments:
	              --------------------------------------------------------------
	mel:          The genome sequence of the Drosophila Melanogaster, with which
	 			  the algorithm starts it's mutation sequence.
	              --------------------------------------------------------------
	mir:          The genome sequence of the Drosophila Miranda, which is the
				  intended target of the sorts on the Melanogaster.
				  The algorithm stops once it has sorted the Melanogaster-
				  sequence into the genome sequence of the Miranda.
	              --------------------------------------------------------------

				  Visualisation:
				  --------------------------------------------------------------
				  The algorithm prints out every swap it makes when sorting the
				  genome-sequence.
				  --------------------------------------------------------------

	              Returns:
	              --------------------------------------------------------------
	mel:     	  The original Melanogaster-sequence that has been sorted into
				  the Miranda-sequence.
	              --------------------------------------------------------------
	'''
	# Open results testfile
	with open('resultaten/pancakeSort.txt', 'w') as f:

		print('PANCAKE SORT', file=f)

		# Visualisation
		print("Start off with:", mel)
		print(' '.join(('Start off with Mel:', str(mel))), file=f)
		print("Run algorithm so that Mel turns in to Mir:", mir)
		print(' '.join(('Run algorithm so that genome-sequence turns in to Mir:'
			    , str(mir))), file=f)

		swapCount = 1
		mel_len = len(mel)
		mir_len = len(mir)

		# Give error message if genome sequences are not of equal length
		if mel_len is not mir_len:
			message = "error, lists are not the same length"
			return message

		# If the seqeunces are of equal length: 'start' the algorithm
		else:
			for i in range(mel_len):
				# If the value in mel on position i is not the value in mir on
				# the same position:
				if mir[i] is not mel[i]:
					# Search trough mel from current position to find the value
					for j in range(i,mel_len):
						# When the value is found, perform a swap so that the
						# value ends up on the correct position
						if mir[i] is mel[j]:
							mel = helper.swapMel(i,j,mel)

							# Visualisation
							print("Swap", swapCount, ":", mel)
							print(' '.join(('Swap', str(swapCount), ":",
								  str(mel))), file=f)
							swapCount += 1

		# Visualisation
		print("Number of swaps:", swapCount - 1)
		print(' '.join(('Number of swaps:', str(swapCount - 1))), file=f)
		print("Final Swap:")
		print(' '.join(('Final Swap:', str(mel))), file=f)

		return mel, swapCount - 1
