letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
letter_number = {letters: index for index, letters in enumerate(letters)}
number_letter = {index:letter for letter, index in letter_number.items()}


def get_original_text(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
    return content

def get_shifamount():
    return int(input("How much should it shift by?"))

def cipher_text(text, shift):
    result = []
    for char in text:
        if char in letter_number:
            current_index = letter_number[char]
            if char.islower():
                new_index = (current_index + shift) % 26 + 26
            else:
                new_index = (current_index + shift) % 26
            result.append(number_letter[new_index])
        elif char == " ":
            result.append(char)
    return ''.join(result)


        