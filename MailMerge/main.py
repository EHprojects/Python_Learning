# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt", "r") as letter_input:
    starting_letter = letter_input.readlines()

# print(starting_letter)

with open("./Input/Names/invited_names.txt", "r") as name_input:
    invite_names = name_input.readlines()

names_stripped = []

for name in invite_names:
    names_stripped.append(name.strip("\n"))

# print(names_stripped)

output_letters = []

for name in names_stripped:
    output = []
    new_addressee_line = starting_letter[0].replace("[name]", name)
    output.append(new_addressee_line)
    for line in starting_letter[1:]:
        output.append(line)
    output_letters.append(output)

# print(output_letters)
# print(len(output_letters))

for i in range(len(output_letters)):
    with open(f"./Output/ReadyToSend/{names_stripped[i]}.txt", "w") as letter_out:
        letter_out.writelines(output_letters[i])
