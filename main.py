with open("./Input/Names/invited_names.txt") as names:
    all_names = names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()
    for name in all_names:
        stripped_name = name.strip()
        final_letter = letter_content.replace("[name]", stripped_name)
        with open(f"./Output/ReadyToSend/{stripped_name}", mode="w") as file:
            file.write(final_letter)
