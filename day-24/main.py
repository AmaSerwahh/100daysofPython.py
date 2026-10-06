#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt") as names:
    names_list = names.readlines()

with open("./Input/Letters/starting_letter.txt") as letters:
    letters_list = letters.read()
    for name in names_list:
        stripped_name = name.strip()
        letter = letters_list.replace("[name]", stripped_name)
        with open(f"./Output/ReadyToSend/Invitation to {stripped_name}.txt", "w") as invitation:
            invitation.write(letter)
