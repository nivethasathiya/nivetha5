def num_Power(N,k):
    if A <= 0 or B <=0:
        print "not a valid input"
    else:
        for i in range (1,20):
            x = B**i
            if x == A :
                print " True "
                print B, "power ", i , "is", A
                break
            elif x> A:
                print "false"
                break

num_Power(244140625,5)
num_Power(4096, 16)
num_Power(0, 16)
num_Power(1,1)
