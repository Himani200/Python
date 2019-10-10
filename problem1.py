#!usr/bin/python3

#Take the name and age as an input from the user and display the year in which the user will turn 95 years old

name = input("Enter your name:")
age = input("Enter your age:")
Age = int(age)
if Age>95:
  year=str(2019-(Age-95))
  print(name+"You have turned 95 in" +year)
else:
  year = str(2019 + (95 - Age))
  print(name + " you will turn 95 years old in " + year)


