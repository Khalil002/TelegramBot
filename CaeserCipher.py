
alphabet = "abcdefghijklmnopqrstuvwxyz"
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SPECIAL_CHARS = " ,.-;:_?!="

def encrypt(plain_text, key):

    cipher_text = ""
    for letter in plain_text:
        if letter in SPECIAL_CHARS:
            cipher_text += letter
            continue
        if letter.isupper():
            print(letter)
            index = ALPHABET.find(letter.upper())
            new_index = flatten(index + key)
            cipher_text += ALPHABET[new_index]
        else:
            index = alphabet.find(letter.lower())
            new_index = flatten(index + key)
            cipher_text += alphabet[new_index]
        
    return cipher_text

def decrypt(cipher_text, key=None):

    if key is None:
        key = find_key_from_cipher(cipher_text)

    plain_text = ""
    for letter in cipher_text:
        #Skipping special characters (incomplete solution)
        if letter in SPECIAL_CHARS:
            plain_text += letter
            continue
        if letter.isupper():
            index = ALPHABET.find(letter.upper())
            new_index = flatten(index - key)
            plain_text += ALPHABET[new_index]
        else:
            index = alphabet.find(letter.lower())
            new_index = flatten(index - key)
            plain_text += alphabet[new_index]
        

    return plain_text

def flatten(number) :

    return number - (26*(number//26))


def find_key_from_cipher(cipher_text):
    index_of_most_common_letter = 4 #Index of 'e'

    #Calculate distribution
    distribution_dict = analyse_letter_distribution(cipher_text)
    #Get common letters
    common_letters = sorted(distribution_dict, key=distribution_dict.get, reverse=True)

    #Use most common letter to get key
    key = ALPHABET.find(common_letters[0]) - index_of_most_common_letter
    return key

def analyse_letter_distribution(cipher_text):
    distribution_dict = {}
    for letter in cipher_text:
        uletter = letter.upper()
        if uletter in SPECIAL_CHARS:
            continue
        if uletter not in distribution_dict:
            distribution_dict[uletter] = 1
        else:
            distribution_dict[uletter] += 1
    if len(distribution_dict.values()) != len(distribution_dict.values()):
        print("Multiple letters appear the same amount of times! Uh oh.")
    return distribution_dict
