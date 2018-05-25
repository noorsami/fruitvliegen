class score:

    def scoreNeighbours(mel):
        '''
            This scorefunction gives a higher score if an element in the list 
            has neighbours which differ 1

            Argument: A list

            returns: a score (int) 

        '''
        score = 0
        length = len(mel)

        # from 1 to length - 1 to avoid giving points if the last element and 
        # the first element differ 1
        for i in range(1, length - 1):

            # compare left / right
            checkLeft = mel[i] - mel[i - 1]
            checkRight = mel[i] - mel[i + 1]
            
            # add 1 to score if the difference is 1
            if abs(checkLeft) == 1:
                score += 1
            if abs(checkRight) == 1:
                score += 1
        return score

    def scoreNeighboursModifier(mel):
        '''
            This scorefunction searches a list and gives a score for n**2 with n the length
            of a series of number which differ 1

            Argument: A list

            returns: A score (int)
        '''

        score = 0
        length = len(mel)
        n = 0

        # length-1 because it compares 2 elements
        for i in range(length - 1):
            check = mel[i] - mel[i + 1]

            if abs(check) == 1:
                n += 1
            else:
                score += n*n
                n = 0
        return score

    def scoreNeighboursList(swapList, scoreList, mir):

    	length = len(swapList)
    	for swap in swapList:
    		score = 0

    		for j in range(len(mir)-1):

    			checkLeft = swap[j] - swap[j - 1]
    			checkRight = swap[j] - swap[j + 1]
    			# does position to check has the right neighbours? if yes add score
    			if abs(checkLeft) == 1:
    				score += 1
    			if abs(checkRight) == 1:
    				score += 1
    		scoreList.append(score)
    	return scoreList
