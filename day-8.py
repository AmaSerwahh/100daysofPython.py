alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(text_message, shift_number, direction):
    cipher_text = ""
    for letter in text_message:
        if letter in alphabet:
            alphabet_index = alphabet.index(letter)
            if direction == "encode":
                shift_index = alphabet_index + shift_number
                new_letter = alphabet[shift_index]
                cipher_text += new_letter
            elif direction == "decode":
                shift_index = alphabet_index - shift_number
                new_letter = alphabet[shift_index]
                cipher_text += new_letter
        else:
            cipher_text += letter

    print(f"The {direction}d text is {cipher_text}")

play_again = True
while play_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift %= 26

    caesar(text, shift, direction)

    go_again = input("Do you want to go again? (y/n):\n").lower()
    if go_again == "n":
        play_again = False
