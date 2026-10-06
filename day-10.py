def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    num1 = float(input("Type a number:\n"))
    end = False
    while not end:
        num2 = float(input("Type the next number:\n"))
        for operator in operations:
            print(operator)
        symbol = input("Pick an operator\n")

        operand = operations[symbol]
        result = operand(num1, num2)
        print(f"{num1} {symbol} {num2} = {result}")

        exit = input(f"Type 'y' to continue calculating with {result} or"
                     f" 'n' to start afresh or 'exit' to exit:\n")
        if exit == "y":
            num1 = result
        elif exit == "n":
            end = True
            calculator()
        else:
            end = True

calculator()
