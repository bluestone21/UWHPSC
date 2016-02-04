def makesqrt(x=4,kmax=100,s=1.0,tol=1.0e-14):
    for k in range(kmax):
        s0 = s
        s = 0.5 * (s + x/s)
        delta_s = s-s0
        if abs(delta_s/x) < tol:
            break

    print "It took %s iterations" %(k)
    return s
