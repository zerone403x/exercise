#!/usr/bin/env python
import string
import keyword

alphas=string.letters+"_"
nums=string.digits

print "Welcome to the Identifier Checker v1.0"
print "Testees must be at least 1 chars long."

myInput=raw_input('Identifier to test?')

if len(myInput)>0:
    if myInput in keyword.kwlist:
        print "Sorry, but what you input is a keyword"
    else:
        if myInput[0] not in alphas:
            print "invalid: first symbol must be alphabetic or _"
        else:
            for otherChar in myInput[1:]:
                if otherChar not in alphas+nums:
                    print "invalid: remaining symbol must be alphanumeric"
                    break
            else:
                print "Okey as an identifier!"

else:
    print "You input nothing"
