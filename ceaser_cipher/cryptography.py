letters = ["a","b","c","d","e","f","g","h","i","j","k,","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]



def encode(string, shift):
    encoded = ""
    for num in range(0, len(string)):
        letter_index = letters.index(string[num]) + shift
        if letter_index > 26:
            letter_index -= 26
        encoded += letters[letter_index]
    return encoded
    
def decode(string, shift):
    decoded = ""
    for num in range(0, len(string)):
        letter_index = letters.index(string[num]) - shift
        if letter_index < 0:
            letter_index += 26
        decoded += letters[letter_index]
    return decoded
