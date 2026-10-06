scores = input("Input a list of scores\n").split()
for n in range(0, len(scores)):
    scores[n] = int(scores[n])
print(scores)

highest = 0
for score in scores:
    if score > highest:
        highest = score
print(f"The highest score is {highest}")