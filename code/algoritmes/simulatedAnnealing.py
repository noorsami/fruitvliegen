from helper import helper
import random as rm
import math as m
import sys
import copy
import time
import matplotlib.pyplot as plt
import numpy as np

def mutateSingle(mel):
    mel_len = len(mel)

    a = rm.randint(0, mel_len - 1)
    b = rm.randint(0, mel_len - 1)

    swappedMel = helper.swapped(a,b,mel)

    return swappedMel


def scoreNeighbours2(mel):

    length = len(mel)
    score = 0

    for i in range(length-1):
    	checkLeft = mel[i] - mel[i - 1]
    	checkRight = mel[i] - mel[i + 1]

    	# does position to check has the right neighbours? if yes add score
    	if abs(checkLeft) == 1:
    		score += 1
    	if abs(checkRight) == 1:
    		score += 1
    return score

def makeTuple(tupleSwap, scoreList, swapList):
	for i in range(len(swapList)):
		tupleSwap.append((scoreList[i], swapList[i]))

	return tupleSwap

def simulatedAnnealing(mel, mir, failValue):

    curScore = 0
    swaps = 0
    failCount = 0
    curMel = mel

    swapHistory = [mel]
    scoreHistory = [0]

    while curMel != mir:

        mutatedMel = mutateSingle(curMel)
        mutatedScore = scoreNeighbours2(mutatedMel)

        if mutatedScore > curScore:
            print("Found better mutation!")

            curMel = mutatedMel
            curScore = mutatedScore

            print(curMel)

            swapHistory.append(curMel)
            scoreHistory.append(curScore)
            swaps += 1

        if mutatedScore == curScore or mutatedScore == (curScore - 1):
            failCount += 1

            marge = int(failValue * 0.001)
            if failCount % failValue in range(0, marge):
                print("                                                                       Herberekening route.")

                curMel = mutatedMel
                curScore = mutatedScore

                print(curMel)

                swapHistory.append(curMel)
                scoreHistory.append(curScore)
                swaps += 1

        if mutatedScore < curScore:
            failCount += 1

    history = makeTuple([], scoreHistory, swapHistory)

    for i in range(len(scoreHistory)):
        print("Mutation: ", swapHistory[i], "Score: ", scoreHistory[i], "Swaps: ", i)

    return history

mel = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
mir = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

test1 = [1,5,3,2,4]
test2 = [1,2,3,4,5]

# simulatedAnnealing(mel, mir, 1000)
