import time

list=[0,1,2,3,4]

print "please input 5 number"
for j in range(len(list)):
    list[j]=input('the '+str(j+1)+' number:')

while True:
    option=raw_input("please choose what do you want \
				input 1 for sum of these numbers \
				input 2 for average of these numbers \
				input X for exit:")
    #print type(option)
    if option=='1':
        print "the sum of these 5 number is %f"%(sum(list))
        break
    elif option=='2':
        print "the average number of these 5 number is %f"%(sum(list)/len(list))
        break
    elif option=='X':
        print "exit!"
        time.sleep(3)
        break
    else:
        print "sorry, I can not understand your input, please re-input"
        continue