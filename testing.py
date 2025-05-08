letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
letter_number = {letters: index for index, letters in enumerate(letters)}

number_letter = {index:letter for letter, index in letter_number.items()}


def shift_text(text, shift):
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

text = "I came, I saw, I conquered!"
shifted = shift_text(text, 20)
print(shifted)

        