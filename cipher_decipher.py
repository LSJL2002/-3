from argparse import ArgumentParser

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
letter_number = {letters: index for index, letters in enumerate(letters)}
number_letter = {index:letter for letter, index in letter_number.items()}


def get_original_text(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
    return content

def get_shift_amount():
    parser = ArgumentParser()
    parser.add_argument("-sh", "--shift", type=int, help="Shift amount for the cipher")
    args = parser.parse_args()
    if args.shift:
        return args.shift
    return int(input("Shift Amount: "))


def cipher(text, shift):
    result = []
    for i,char in enumerate(text):
        if i%5 == 0 and i != 0: 
            result.append(" ")
        if char in letter_number:
            current_index = letter_number[char]
            if char.islower():
                new_index = (current_index - shift) % 26 + 26
            else:
                new_index = (current_index - shift) % 26
            result.append(number_letter[new_index])
    return ''.join(result)

def cipher_with_ascii(text, shift):
    result = []
    for i,char in enumerate(text):
        if i%5 == 0 and i != 0: 
            result.append(" ")
        if char.islower():
            new_char = chr((ord(char)-97-shift)%26+97)
        else:
            new_char = chr((ord(char)-65-shift)%26+65)
        result.append(new_char)
    return ''.join(result)
    
def remove_nonletters(text):
    return ''.join(char for char in text if char in letter_number)

def decipher(text, shift):
    text = remove_nonletters(text)
    result = []
    for char in text:
        current_index = letter_number[char]
        if char.islower():
            new_index = (current_index + shift) % 26 + 26
        else:
            new_index = (current_index + shift) % 26
        result.append(number_letter[new_index])
    return ''.join(result)

def decipher_ascii(text,shift):
    text = remove_nonletters(text)
    result = []
    for i,char in enumerate(text):
        if char.islower():
            new_char = chr((ord(char)-97+shift)%26+97)
        else:
            new_char = chr((ord(char)-65+shift)%26+65)
        result.append(new_char)
    return ''.join(result)

if __name__ == "__main__":
    original_text = get_original_text("text.txt")
    shift = get_shift_amount()
    letter_only = remove_nonletters(original_text)
    cipher_text = cipher_with_ascii(letter_only, shift)
    print(f"{cipher_text=}")
    deciphered_text = decipher_ascii(cipher_text, shift)
    print(f"{deciphered_text=}")