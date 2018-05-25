class score:

    def scoreNeighbours(mel):
        '''
            Function for calculating the score of a genome sequence

        	                Arguments:
            	            ----------------------------------------------------
            mel:            The genome sequence where to start from.

                            Returns:
                            ----------------------------------------------------
            score:          The score that is returned from the scorefunction.
        '''
        score = 0
        length = len(mel)
        # goes through the list
        for i in range(1, length - 1):

            # checks the values from the left and the right of index
            checkLeft = mel[i] - mel[i - 1]
            checkRight = mel[i] - mel[i + 1]

            # value next to index has to differ with a size of 1 to get asigned
            if abs(checkLeft) == 1:
                score += 1
            if abs(checkRight) == 1:
                score += 1

        return score

    def scoreNeighboursModifier(mel):

        score = 0
        length = len(mel)
        n = 0
        for i in range(length - 1):
            check = mel[i] - mel[i + 1]

            if abs(check) == 1:
                n += 1
            else:
                score += n*n
                n = 0
        return score

    def scoreNeighboursList(swapList, scoreList, mir):
        '''
            Function for calculating the score of a genome sequence

                	        Arguments:
                    	    ----------------------------------------------------
            swapList:       The generated list filled with N random swapped
                            lists from Mel.

            scoreList:      For the definition of an empty list

                            Returns:
                            ----------------------------------------------------
            scoreList:      A list filled with scores. The index of the scoreList
                            connects with the index of the swapList.
        '''
    	length = len(swapList)
        # for each list in the swaplist
    	for swap in swapList:
    		score = 0
            # for each item in the list
    		for j in range(24):

                # checks the values from the left and the right of index
    			checkLeft = swap[j] - swap[j - 1]
    			checkRight = swap[j] - swap[j + 1]

                # value next to index has to differ with a size of 1 to get asigned
    			if abs(checkLeft) == 1:
    				score += 1
    			if abs(checkRight) == 1:
    				score += 1

    		scoreList.append(score)

    	return scoreList
