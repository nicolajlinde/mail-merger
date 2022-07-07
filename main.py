# # TODO: Create a letter using starting_letter.txt
# all_names = []
# l1 = []
# with open("./Input/Letters/starting_letter.txt", "r") as lines:
#     letter = lines.readlines()
#
# # for each name in invited_names.txt
# with open("./Input/Names/invited_names.txt") as file:
#     for name in file:
#         x = name.strip("\n")
#         all_names.append(x)
#
# for i in range(len(all_names)):
#     # Replace the [name] placeholder with the actual name.
#     r = letter[0].replace("[name]", all_names[i])
#     l1.append(r)
#
# i = 0
# for n in l1:
#     letter[0] = n
#     with open(f"./Output/ReadyToSend/{all_names[i]}", mode="w") as file:
#         for v in letter:
#             file.write(v)
#     i += 1

with open("./Input/Names/invited_names.txt") as names:
    all_names = names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()
    for name in all_names:
        stripped_name = name.strip()
        final_letter = letter_content.replace("[name]", stripped_name)
        with open(f"./Output/ReadyToSend/{stripped_name}", mode="w") as file:
            file.write(final_letter)
