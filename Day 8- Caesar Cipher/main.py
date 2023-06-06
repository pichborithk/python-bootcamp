from alphabets import alphabet
from art import logo

print(logo)


def caesar(input_text, shift_amount, cipher_direction):
    result = ""
    shift_amount = shift_amount % 26
    if cipher_direction == "decode":
        shift_amount *= -1

    for letter in input_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = index + shift_amount
            result += alphabet[new_index]
        else:
            result += letter

    print(f"The {cipher_direction}d text is {result}")


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(text, shift, direction)
