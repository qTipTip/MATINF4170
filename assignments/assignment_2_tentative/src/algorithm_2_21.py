import numpy as np

def IndexBinary(x, knots):
    """
    given a knot vector and a parameter knots[0] <= x < knots[-1] finds the
    index mu for which knots[mu] <= x < knots[mu+1] using a binary search
    """
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

def BSplinesEvaluation(x, knots, p):
    mu = IndexBinary(x, knots)
    B = assembleR(1, knots, x, mu)
    for k in range(2, p+1):
        R = assembleR(k, knots, x, mu)
        B = np.mat(B)*np.mat(R)
        print(B)

def assembleR(k, knots, x, mu):
    R = np.zeros(shape=(k, mu), dtype=np.float64)
    for i in range(k):
        # not sure about indexing here, seems to work
        R[i][i] = (knots[mu+i+1] - x) / (knots[mu+i+1] - knots[mu+i+1-k])
        R[i][i+1] = (x - knots[mu+1-k]) / (knots[mu+i] - knots[mu+i-k])
    return R



if __name__ == "__main__":
   knots = range(100) 
   p = 3
   x = 7.0
   BSplinesEvaluation(x, knots, p)
