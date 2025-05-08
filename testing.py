letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
letter_number = {letters: index for index, letters in enumerate(letters)}

number_letter = {index:letter for letter, index in letter_number.items()}


def cipher(text, shift):
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


def remove_nonletters(text):
    return ''.join(char for char in text if char in letter_number)

def decipher(text, shift):
    result = []
    for char in text:
        current_index = letter_number[char]
        if char.islower():
            new_index = (current_index - shift) % 26 + 26
        else:
            new_index = (current_index - shift) % 26
        result.append(number_letter[new_index])

    return ''.join(result)

if __name__ == "__main__":
    original_text = "I came, I saw, I conquered!"
    shift = 20  
    letter_only = remove_nonletters(original_text)
    cipher_text = cipher(letter_only, shift)
    print(f"{cipher_text=}")
    deciphered_text = decipher(cipher_text, shift)
    print(f"{deciphered_text=}")