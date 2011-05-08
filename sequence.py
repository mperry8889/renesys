#!/usr/bin/env python
import string

def getStrippedLetter(word):
    for letter in word:
        if letter not in string.punctuation:
            return letter

def sequence(string, exceptions=1):
    if exceptions < 0:
        raise AttributeError, "Number of exceptions must be >= 0"
    
    # get a list of the words' first letter
    words = string.split(" ")
    letters = [getStrippedLetter(word) for word in words]    

    # generate comparisons for every (x, y) pair in the list of letters.
    # the zip here is a little bit of magic to create a pairing of 
    # every two sequential items in the list.  the end result will be
    # an array of [True, False, etc.]
    comparisons = [y.lower() >= x.lower() for (x, y) in zip(letters, letters[1:])]
   
    # now just find the longest sequence that has at most "exceptions" number
    # of Falses.  This handles the ordering resets implicitly, thankfully without
    # the need for all kinds of state or tracking variables.
    longestSequenceIndex = 0
    longestSequenceLength = 1
    
    for i, root in enumerate(comparisons):
        
        # we will assume that the exception cannot be
        # in the first element
        if root is False:
            continue
        
        usedExceptions = 0
        
        for j, sequenceEndpoint in enumerate(comparisons[i:]):
            currentSequenceLength = j+1
            
            if sequenceEndpoint is False:
                usedExceptions += 1
                if usedExceptions > exceptions:
                    break
            
            if currentSequenceLength > longestSequenceLength:
                longestSequenceLength = currentSequenceLength
                longestSequenceIndex = i

    # return a string of words with the longest sequence.  the +1 is because the code is looking for
    # the longest sequence of comparisons. so we need to add one to add the ending word to the result
    return " ".join(words[longestSequenceIndex : (longestSequenceIndex + longestSequenceLength + 1)])

if __name__ == "__main__":
    import sys
    print sequence(sys.argv[1])