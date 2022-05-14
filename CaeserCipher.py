
alphabet = "abcdefghijklmnñopqrstuvwxyz"
ALPHABET = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
SPECIAL_CHARS = " .,-_():;¡!¿?1234567890#$%&/=*+}[]{><áéíóú"
SPECIAL_CHARS = SPECIAL_CHARS+'"'
SPECIAL_CHARS = SPECIAL_CHARS+"'"

def encrypt(plain_text, key):

    cipher_text = ""
    for letter in plain_text:
        if letter in SPECIAL_CHARS:
            index = SPECIAL_CHARS.find(letter)
            new_index = flatten(index + key, 44)
            cipher_text += SPECIAL_CHARS[new_index]
        elif letter.isupper():
            index = ALPHABET.find(letter.upper())
            new_index = flatten(index + key, 26)
            cipher_text += ALPHABET[new_index]
        else:
            index = alphabet.find(letter.lower())
            new_index = flatten(index + key, 26)
            cipher_text += alphabet[new_index]
    
    print("")
    print("Encryption")
    print('shift: ', key)
    print(plain_text)
    print(cipher_text)
    
    return cipher_text

def decrypt(cipher_text, key=None):

    if key is None:
        key = find_key_from_cipher(cipher_text)

    plain_text = ""
    for letter in cipher_text:
        #Skipping special characters (incomplete solution)
        if letter in SPECIAL_CHARS:
            index = SPECIAL_CHARS.find(letter)
            new_index = flatten(index - key, 44)
            plain_text += SPECIAL_CHARS[new_index]
        elif letter.isupper():
            index = ALPHABET.find(letter.upper())
            new_index = flatten(index - key, 26)
            plain_text += ALPHABET[new_index]
        else:
            index = alphabet.find(letter.lower())
            new_index = flatten(index - key, 26)
            plain_text += alphabet[new_index]
    
    print("")
    print("Decryption")
    print('key: ',key)
    print(plain_text)
    return plain_text

def flatten(number, size) :
    return number - (size*(number//size))


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
    
    modified_text = cipher_text
    for c in SPECIAL_CHARS:
        modified_text = modified_text.replace(c, '')
    
    print('Modified text: ',modified_text)
    distribution_dict = {}
    for letter in modified_text:
        
        uletter = letter.upper()
        
        if uletter not in distribution_dict:
            distribution_dict[uletter] = 1
        else:
            distribution_dict[uletter] += 1
            
    if len(distribution_dict.values()) != len(distribution_dict.values()):
        print("Multiple letters appear the same amount of times! Uh oh.")
    return distribution_dict
