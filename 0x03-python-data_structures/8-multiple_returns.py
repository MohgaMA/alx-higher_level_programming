#!/usr/bin/python3
def multiple_returns(sentence):
    if (len(sentence) == 0):
        tupl = (len(sentence), None)
    else :
        tupl = (len(sentence), sentence[0])
    return (tupl)
