#!usr/bin/python3

import subprocess
import os
import sys

choice=input("Enter a command? y/n :")
while choice == 'y':  
	cmd=input("enter command:")
#arg=input("enter atrribute if any :")
#mycmd=[cmd,arg]
	mycmd=[cmd]

	f=open('prob8f.txt','a')
	f.write(cmd)
	f.write('\n')
	f.close()


	code=subprocess.call(mycmd)
	if code >0:
		print(sys.stderr," execution failed: ",code)	

	choice=input("Enter a command? y/n :")


