import random

name = input("Give me the names of everyone, separated by a comma\n")
names = name.split(', ')
#print(names)

number_of_persons = len(names)
#print(number_of_persons)

pay = random.randint(0,number_of_persons - 1)
print(f"{names[pay]} is going to buy the meal today")
