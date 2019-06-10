#!usr/bin/python3

import webbrowser
from googlesearch import search

f=open("file1.txt","w")
web = input("Enter topic:")
x = search(web,stop=3)
for i in x:
	f.write(i + "\n")
webbrowser.open("https://www.google.com/search?q="+ web)
