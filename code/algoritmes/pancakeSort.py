from helper import helper
import time
import matplotlib.pyplot as plt



def pancakeSort(mel, mir):

	with open(“resultaten/pancakeSort.txt”) as results:

		print("Start off with Mel:", mel)


		results.write("Start off with Mel:", mel)


		time.sleep(0.5)
		print("Run algorithm so that Mel turns in to Mir:", mir)

		results.write("Run algorithm so that Mel turns in to Mir:", mir)
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
							print("Swap", swapCount, ":", mel)
							results.write("Swap", swapCount, ":", mel)

							swapCount += 1
							time.sleep(0.5)

		print("Number of swaps:", swapCount - 1)
		results.write("Number of swaps:", swapCount - 1)
		print("Final Swap:")

		results.write("Final Swap:", mel)


	return mel
