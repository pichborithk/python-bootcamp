# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt") as invited_data:
    invited_list = invited_data.readlines()


with open("./Input/Letters/starting_letter.txt") as letters_data:
    content = letters_data.read()


for name in invited_list:
    new_content = content.replace("[name]", name.strip())
    with open(
        f"./Output/ReadyToSend/letter_for_{name.strip()}.txt", mode="w"
    ) as letter:
        letter.write(new_content)
