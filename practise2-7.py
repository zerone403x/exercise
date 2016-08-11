x = raw_input('please input a string:')

print "this is while loop"
i=0
while i<len(x):
    print x[i],
    i+=1

print
print "this is for loop"
for j in x:
    print j,