height = int(input("Height of wall:\n"))
width = int(input("Width of wall:\n"))
coverage = 5

def paint_calc(h, w, c):
    cans = (h * w)/c
    print(f"You will need {cans} cans of paint")

paint_calc(height, width, coverage)