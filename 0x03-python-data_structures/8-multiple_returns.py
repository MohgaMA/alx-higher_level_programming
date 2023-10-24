#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if (length == 0):
        _tuple = (0, "None")
    else:
        _tuple = (length, sentence[0])
    return _tuple
