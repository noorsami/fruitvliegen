from helper import helper


def pancakeSort(mel, mir):
	swapCount = 0
	mel_len = len(mel)
	mir_len = len(mir)
	if mel_len is not mir_len:
		message = "error, lists are not the same length"
		return message
	else:
		for i in range(mel_len):


			if mir[i] is not mel[i]:


				for j in range(i,mel_len):


					if mir[i] is mel[j]:
						mel = helper.swapMel(i,j,mel)
						swapCount += 1
						print(mel)
	print("Final swap: ", mel)
	print("swaps: ", swapCount)

	return mel