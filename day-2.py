print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n$"))
tip = float(input("what percentage tip would you like to give?\n$"))
tip = (tip/100) * bill
persons = int(input("How many people to split the bill?\n"))

total_bill = (bill + tip)/persons
print(f"Each person should pay: ${total_bill:.2f}")