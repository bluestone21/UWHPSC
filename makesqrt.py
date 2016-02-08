def makesqrt(x,kmax=100, s=1.0, tol=1.0e-14, debug=False):
    if x == 0:
        print "***WARNING***: Zero Entered, Return Value is Zero"
        return 0
    elif x<0:
        print "***Error***: Negative Number Entered For Square Root"
    elif x>0:
        for k in range(kmax):
            s0 = s
            s = 0.5 * (s + x/s)
            delta_s = s-s0
            if abs(delta_s/x) < tol:
                break

        if debug:
            print "It took %s iterations" %(k)
        return s
