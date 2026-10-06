print("Welcome to the love calculator!")
name1 = input("what is your name?\n").lower()
name2 = input("What is their name?\n").lower()

name1true = name1.count("t") + name1.count("r") + name1.count("u") +name1.count("e")

name1love = name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e")


name2true = name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e")

name2love = name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")

score = int(str(name1true + name1love) + str(name2true + name2love))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}, you are not alright together")