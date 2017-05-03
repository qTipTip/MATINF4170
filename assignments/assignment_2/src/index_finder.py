import numpy as np
import time
def IndexNaive(x, knots):
    for i in range(len(knots)-1):
        if knots[i] <= x < knots[i+1]:
            return i
    return i

def IndexEvaluation(x, knots, previous=0):
    for i in range(previous, len(knots-1)):
        if knots[i] <= x < knots[i+1]:
            return i

def IndexBinary(x, knots):
    a = 0
    b = len(knots)-1

    while a <= b:
        c = (a + b) // 2
        if knots[c] <= x < knots[c+1]:
            return c
        else:
            if x < knots[c]:
                b = c - 1
            else:
                a = c + 1
def IndexBinaryEvaluation(x, knots, previous=0):
    a = previous
    b = len(knots)-1

    while a <= b:
        c = (a + b) // 2
        if knots[c] <= x < knots[c+1]:
            return c
        else:
            if x < knots[c]:
                b = c - 1
            else:
                a = c + 1
