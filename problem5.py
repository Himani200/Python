#!usr/bin/python3


import datetime

name=input("Enter your name:")

currentTime = datetime.datetime.now()
t = currentTime.hour

if t < 13:
	print("Good morning "+ name)

elif t > 12 and t < 18:
	print("Good afternoon "+name)

elif t > 17 and t < 21:
        print("Good evening "+name)

else :
        print("Good night "+name)




