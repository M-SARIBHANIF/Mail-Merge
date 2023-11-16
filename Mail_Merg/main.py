place_holder = "[name]"
with open("./Input/Names/invited_names.txt") as names_data:
    names = names_data.readlines()
with open("./Input/Letters/starting_letter.txt") as letter_data:
    letter_contents = letter_data.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(place_holder, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}", mode="w") as final_letter:
            final_letter.write(new_letter)



