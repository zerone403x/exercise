def _2dExp(height,fold):
	#single_h = height/(2**fold)
	try:
		area = int(height)*2**int(fold)
	except:
		print type(height),type(fold),type(area)
	
	return area
	

cube_h = raw_input("please input cube height:")
fold_count = raw_input("please input fold counters:")

print _2dExp(cube_h,fold_count)