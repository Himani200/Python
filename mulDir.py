#!usr/bin/python3

import os



for i in range(100):
	dirName =str(i)
	try:
		os.mkdir(dirName)
		print("Directory " , dirName , "created")
	except FileExistsError:
		print("Directory" , dirName , "already h")
