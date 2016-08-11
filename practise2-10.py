while True:
    x=input("please input a number between 1~100:")
    if 1<=x<=100:
        print "the %d you input is between 1~100, thank you"%(x)
        break
    else:
        print "Sorry, the %d you input is not between 1~100, please re-input"%(x)
        continue