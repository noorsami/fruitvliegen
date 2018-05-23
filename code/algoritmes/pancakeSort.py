from helper import helper
import time
import matplotlib.pyplot as plt


def pancakeSort(mel, mir):

	# open results textfile
	with open('resultaten/pancakeSort.txt', 'w') as f:

		print('PANCAKE SORT', file=f)

		# visualization
		print("Start off with:", mel)
		print(' '.join(('Start off with Mel:', str(mel))), file=f)

		time.sleep(0.5)

		# visualization
		print("Run algorithm so that Mel turns in to Mir:", mir)
		print(' '.join(('Run algorithm so that genome-sequence turns in to Mir:', str(mir))), file=f)
		time.sleep(0.5)

		swapCount = 1
		mel_len = len(mel)
		mir_len = len(mir)
		if mel_len is not mir_len:
			message = "error, lists are not the same length"
			return message
		else:
			for i in range(mel_len):

				# if position value in mel is not position value in mir
				if mir[i] is not mel[i]:
					# search from position through mel to find the value
					for j in range(i,mel_len):
						# when found swap
						if mir[i] is mel[j]:

							mel = helper.swapMel(i,j,mel)

							# visualization
							print("Swap", swapCount, ":", mel)
							print(' '.join(('Swap', str(swapCount), ":", str(mel))), file=f)

							swapCount += 1
							time.sleep(0.5)

		# visualization
		print("Number of swaps:", swapCount - 1)
		print(' '.join(('Number of swaps:', str(swapCount - 1))), file=f)
		print("Final Swap:")
		print(' '.join(('Final Swap:', str(mel))), file=f)

		return mel
