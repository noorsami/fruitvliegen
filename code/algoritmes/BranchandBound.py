import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))

from helper import helper

def branchAndBound(solutions, bound, mir, mel):

    '''
        This function tries a branch and bound approach to change one list in another using swaps.
        It doesn't break a series of numbers which differs only 1 with its neighbours

        Arguments: amount of solutions wanted (int), bound for how deep the search goes (int),
                    the two lists which need to be changed

        Returns: the solutionhistory

    '''
    stack = []
    mir = [tuple(mir)]
    randSeq = helper.makeSequence(tuple(mel))
    stack.append([randSeq])
    history = []


    # while stack not empty and solutions > 1
    while stack and solutions:

        current = stack.pop()

        # check whether current is too deep
        if len(current) < bound:

            # make all possible changes without breaking sequences
            allSwaps = helper.swapAllSequence(current[-1])


            for swap in allSwaps:

                # make new sequences [[1,2],[3],...] -> [[1,2,3],...]
                swap = helper.makeSequence(helper.makeList(swap))

                if swap == mir:

                    # add to history and bound is current length
                    history.append(current + [swap])
                    bound = len(current)
                    solutions -= 1



                stack.append(current + [swap])
    return history