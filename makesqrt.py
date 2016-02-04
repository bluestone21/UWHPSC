def makesqrt(x,k=100,s=1.0):
    for i in range(k):
        s = 0.5 * (s + x/s)

    return s
