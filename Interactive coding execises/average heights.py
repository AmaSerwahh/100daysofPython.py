heights = input("Input a list of heights:\n").split()
for n in range(0, len(heights)):
    heights[n] = int(heights[n])
print(heights)

students = 0
total = 0
for h in heights:
    total += h
    students += 1
average = round(total / students)
print(f"The average is {average}")

