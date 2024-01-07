#!/usr/bin/python3
def multiple_returns(sentence):
    length = 0

    if len(sentence) == 0:

        return length, None

    for i in sentence:

        length += 1

    return length, sentence[0]
