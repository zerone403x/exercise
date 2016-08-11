import re

#file_location = ""
reg = r'hello'
tar = "csvt"

def counter(patt,content):
	res=re.findall(patt,content)
	print res
	return len(res)
	
def sub(patt,target,content):
	res=re.sub(patt,target,content)
	print res
	return res

fr = open('a.txt')
con = fr.read()
fr.close()

#print counter(reg,con)
print sub(reg,tar,con)
