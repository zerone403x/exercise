'''pracise of 2-8,2-9'''
list=[0,1,2,3,4]
print "while loop"
print "please input 5 number"
i=0
while i<5:
    list[i]=input('the '+str(i+1)+' number:')
    i+=1
	
print "the sum of these 5 number is %f"%(sum(list))
print "the average number of these 5 number is %f"%(sum(list)/len(list))

print"for loop"
print "please input 5 number"
for j in range(len(list)):
    list[j]=input('the '+str(j+1)+' number:')

print "the sum of these 5 number is %d"%(sum(list))
print "the average number of these 5 number is %f"%(sum(list)/len(list))
