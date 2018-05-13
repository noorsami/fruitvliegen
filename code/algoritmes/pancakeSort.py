from helper import helper
import time
import matplotlib.pyplot as plt

def pancakeSort(mel, mir):

	print("Start off with Mel:", mel)
	print("Run algorithm so that Mel turns in to Mir:", mir)

	swapCount = 1
	mel_len = len(mel)
	mir_len = len(mir)
	if mel_len is not mir_len:
		message = "error, lists are not the same length"
		return message
	else:
		for i in range(mel_len):

			## visualization
			#plt.plot(mir, mel, mir, mir)
			#plt.axis([1,25, 1, 25])
			#plt.show()

			# if position value in mel is not position value in mir
			if mir[i] is not mel[i]:
				# search from position through mel to find the value
				for j in range(i,mel_len):
					# when found swap
					if mir[i] is mel[j]:

						mel = helper.swapMel(i,j,mel)
						print("Swap", swapCount, ":", mel)

						## visualization
						#plt.show()

						swapCount += 1
						time.sleep(0.5)

	print("Number of swaps:", swapCount - 1)
	print("Final Swap:")

	return mel
