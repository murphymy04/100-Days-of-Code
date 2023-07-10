# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt", "r") as l:
    letter = l.readlines()
    with open("../Mail Merge Project Start/Input/Names/invited_names.txt", "r") as n:
        names = n.readlines()
        new_open = []
        new_letters = []
        new_names = []
        for i in names:
            new_name = i.replace("\n", "")
            new_names.append(new_name)
            letter_open = letter[0].replace("[name]", new_name)
            new_open.append(letter_open)
        for i in range(len(names)):
            letter[0] = new_open[i]
            new_letter = "".join(letter)
            new_letters.append(new_letter)
            new_l = open(f"/Users/myles/PycharmProjects/Day-24/Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend/letter_for_{new_names[i]}.txt", "w")
            new_l.write(new_letters[i])
