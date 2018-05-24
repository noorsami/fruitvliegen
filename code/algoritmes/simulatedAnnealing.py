from helper import helper
import random as rm

''' Function for mutating a single mel with random values '''
def mutateSingle(mel):
    mel_len = len(mel)
    a = rm.randint(0, mel_len - 1)
    b = rm.randint(0, mel_len - 1)
    swappedMel = helper.swapped(a,b,mel)
    return swappedMel

''' Function to make a tuple-list for every mutation and score '''
def makeTuple(tupleSwap, scoreList, swapList):
	for i in range(len(swapList)):
		tupleSwap.append((scoreList[i], swapList[i]))
	return tupleSwap

''' Simulated annealing algorithm '''
def simulatedAnnealing(mel, mir, failValue, scoreFunction):
    '''
    A probabilistic algorithm for approximating the global optimum of a given
    function, the global optimum being the final mutation (swap) that changes
    the genome sequence of the Drosophila Melanogaster into the Drosophila
    Miranda.

    The algorithm starts with the genome-sequence of the Drosophila Melanogaster
    and then generates a random mutation on the genome-sequence. If the score of
    the genome sequence is higher than the score of the current mutation
    (Or when starting: the Melanogaster sequence), the generated mutation is the
    new current mutation. This repeats until the Melanogaster is transformed
    into the Miranda.

                      Arguments:
                      ----------------------------------------------------------
    mel:              The genome sequence of the Drosophila Melanogaster, with
                      which the algorithm starts it's mutation sequence.
                      ----------------------------------------------------------
    mir:              The genome sequence of the Drosophila Miranda, which is
                      the intended target of the mutations on the Melanogaster.
                      The algorithm stops once it has mutated the Melanogaster
                      into the genome sequence of the Miranda.
                      ----------------------------------------------------------
    failValue:        The value of the interval of failed mutations (Mutations
                      with a lesser or equal score than the latest mutation) by
                      which the algorithm allows lesser mutations to pass into
                      the mutation sequence, in order to avoid getting stuck on
                      a plateau.
                      ----------------------------------------------------------
    scoreFunction:    The function which the algorithm uses to score each
                      individual mutation.
                      ----------------------------------------------------------

                      Returns:
                      ----------------------------------------------------------
    scoreHistory:     A list of the all the (accepted) generated mutations,
                      including the score of each individual mutation. Each
                      mutation & score is saved in the list as a tuple.
                      ----------------------------------------------------------
    '''

    curScore = 0
    swaps = 0
    failCount = 0
    curMel = mel
    swapHistory = [mel]
    scoreHistory = [0]

    print('---------------------------------------')
    print('SIMULATED ANNEALING: LIVE VISUALIZATION')
    print('---------------------------------------')

    # Repeat the algorithm until mel has been transformed into mir
    while curMel != mir:
        mutatedMel = mutateSingle(curMel)
        mutatedScore = scoreFunction(mutatedMel)

        # If the newly generated score is higher than the current,
        # the mutated mel is the new current mel
        if mutatedScore > curScore:
            print("Found better mutation!")
            curMel = mutatedMel
            curScore = mutatedScore
            print(curMel)
            swapHistory.append(curMel)
            scoreHistory.append(curScore)
            swaps += 1

        # To avoid getting stuck on a plateau, the algorithm allows a mutation
        # with an equal or a mutation with score 1 lower than the latest
        # mutation to pass approximately once every 1000 failed swaps
        if mutatedScore == curScore or mutatedScore == (curScore - 1):
            failCount += 1
            marge = int(failValue * 0.001)
            if failCount % failValue in range(0, marge):
                print((4 * "                 ") +"Trying different route.")
                curMel = mutatedMel
                curScore = mutatedScore
                print(curMel)
                swapHistory.append(curMel)
                scoreHistory.append(curScore)
                swaps += 1

        # If the generated mutation is less than the current score,
        # add 1 to failCount
        if mutatedScore < curScore:
            failCount += 1

    print('--------------------------------')
    print('SIMULATED ANNEALING: SWAPHISTORY')
    print('--------------------------------')

    # Create a list with the history of every accepted mutation and it's score
    history = makeTuple([], scoreHistory, swapHistory)

    # Print full mutation history and the corresponding score for each mutation
    for i in range(len(scoreHistory)):
<<<<<<< HEAD
        print("Mutation: ", swapHistory[i], "Score: ", scoreHistory[i], "Swaps: ", i)
    return history, len(scoreHistory)
=======
        print("Mutation: ", swapHistory[i], "Score: ", scoreHistory[i],
              "Swaps: ", i)
    return history
>>>>>>> fd54c6427e6008ea422c5678f209108ceb7a96e3
