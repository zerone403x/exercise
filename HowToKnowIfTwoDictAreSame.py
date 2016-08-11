# -*- coding:utf-8 -*-

#comfirm whether the two dict is same
earth={'name':'earth','attrib':'planet','size':'small'}
mars={'name':'mars','attrib':'planet','size':'small'}

#method 1
print "this output from method 1"
print cmp(earth,mars)

#method 2
#step 1 whether the length of two dicts are same
cmp(len(earth),len(mars))==0 #or
len(earth)==len(mars)

#step 2 whether all the elements of two dicts.keys() are same
reduce(lambda x,y:x and y,[keys in mars.keys() for keys in earth.keys()])

#step 3 whether all the elements of two dicts.values() are same
print "this output from method 2"
print reduce(lambda x,y:x and y,[values in mars.values() for values in earth.values()])

#refer 《python 核心编程 2》 图7-1