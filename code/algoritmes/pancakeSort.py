from helper import helper
import time
import matplotlib.pyplot as plt 

def pancakeSort(mel, mir):

	print("Start off with Mel:", mel)
	print("Run algorithm so that Mel turns in to Mir:", mir)

	swapCount = 0
	mel_len = len(mel)
	mir_len = len(mir)
	if mel_len is not mir_len:
		message = "error, lists are not the same length"
		return message
	else:
		for i in range(mel_len):

			plt.plot(mir, mel, mir, mir)
			plt.axis([1,25, 1, 25])
			plt.show()

			if mir[i] is not mel[i]:
				for j in range(i,mel_len):
					if mir[i] is mel[j]:
						mel = helper.swapMel(i,j,mel)
						print("Swap", swapCount, ":", mel)

						plt.show()

						swapCount += 1
						time.sleep(0.5)
	print("Final Swap:", mel)
	print("Number of swaps:", swapCount)

	return mel
