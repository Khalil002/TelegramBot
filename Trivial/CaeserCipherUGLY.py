
from operator import mod
import sys
import enchant
from collections import Counter

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
alphabet = "abcdefghijklmnñopqrstuvwxyz"
ALPHABET = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
SPECIAL_CHARS = ".,-_():;¡!¿?1234567890#$%&/=*+}[]{><áéíóú”"
SPECIAL_CHARS = SPECIAL_CHARS+'"'
SPECIAL_CHARS = SPECIAL_CHARS+"'"

def encrypt(plain_text, key):

    cipher_text = ""
    for letter in plain_text:
        if letter == ' ':
            cipher_text += letter
            continue
        else:
            if letter in SPECIAL_CHARS:
                index = SPECIAL_CHARS.find(letter)
                new_index = flatten(index + key, 43) #remember to change to 44 because of space
                cipher_text += SPECIAL_CHARS[new_index]
            elif letter.isupper():
                index = ALPHABET.find(letter.upper())
                new_index = flatten(index + key, 27)
                cipher_text += ALPHABET[new_index]
            else:
                index = alphabet.find(letter.lower())
                new_index = flatten(index + key, 27)
                cipher_text += alphabet[new_index]
        
    
    print("")
    print("Encryption")
    print('shift: ', key)
    print(plain_text)
    print(cipher_text)
    
    return cipher_text

def decrypt3(cipher_text, key=None):
    if key is None:
        key = find_key3(cipher_text)

    plain_text = ""
    for letter in cipher_text:
        if letter == ' ':
            plain_text += letter
            continue
        else:
            #Skipping special characters (incomplete solution)
            if letter in SPECIAL_CHARS:
                index = SPECIAL_CHARS.find(letter)
                new_index = flatten(index - key, 43)
                plain_text += SPECIAL_CHARS[new_index]
            elif letter.isupper():
                index = ALPHABET.find(letter.upper())
                new_index = flatten(index - key, 27)
                plain_text += ALPHABET[new_index]
            else:
                index = alphabet.find(letter.lower())
                new_index = flatten(index - key, 27)
                plain_text += alphabet[new_index]
        
    
    return plain_text

def find_key3(cipher_text):
    words = []
    f = open("Trivial/palabras.txt", "r")
    for line in f:
        words.append(line.rstrip())
    
    modified_text = cipher_text
    for c in SPECIAL_CHARS:
        modified_text = modified_text.replace(c, '')
    
    bestcase = 0
    bestnum = 0
    for i in range(len(alphabet)):
        temp_text = decrypt3(modified_text, i)
        newWords = temp_text.split()
        for b in range(len(newWords)):
            newWords[b] = newWords[b].lower()
        tempnum = 0
        for j in newWords:
            for k in words:
                if(j==k):
                    tempnum=tempnum+1
                    break
        if(tempnum>bestnum):
            bestnum = tempnum
            bestcase = i
    return bestcase
            
                
                    
def deshift(cipher_text, key):
    plain_text = ""
    for letter in cipher_text:
        if letter == ' ':
            plain_text+= letter
            continue
        else:
            #Skipping special characters (incomplete solution)
            if letter in SPECIAL_CHARS:
                index = SPECIAL_CHARS.find(letter)
                new_index = flatten(index - key, 43)
                plain_text += SPECIAL_CHARS[new_index]
            elif letter.isupper():
                index = ALPHABET.find(letter.upper())
                new_index = flatten(index - key, 27)
                plain_text += ALPHABET[new_index]
            else:
                index = alphabet.find(letter.lower())
                new_index = flatten(index - key, 27)
                plain_text += alphabet[new_index]
    
    return plain_text

def Descifrado(texto):
  
    letrasMasUsadas = "EAOSRNIDLCTUMPBGVYQHFZJÑXKW"
    modified_text = texto
    for c in SPECIAL_CHARS:
        modified_text = modified_text.replace(c, '')
    modified_text = modified_text.replace(' ', '')
    
    res = Counter(modified_text)
    res = max(res, key = res.get)
    s=""
    s=s+res
    s=s.upper()
    d = enchant.Dict("es_CO")
  
    llave = 0
    descifrado = ""
    bestcase=0
    for i in letrasMasUsadas:
        
        shift=ALPHABET.find(s)-ALPHABET.find(i)
        decryptedText = deshift(texto, shift)
        words = decryptedText.split()
        count=0
        for word in words:
            if(d.check(word)==True):
                count+=1
        if(count>bestcase):
            llave=shift
            descifrado = decryptedText
            bestcase = count
    return descifrado
        




def decrypt2(cipher_text, key=None):
    if key is None:
        key = find_key2(cipher_text)

    plain_text = ""
    for letter in cipher_text:
        if letter == ' ':
            plain_text+= letter
            continue
        else:
            #Skipping special characters (incomplete solution)
            if letter in SPECIAL_CHARS:
                index = SPECIAL_CHARS.find(letter)
                new_index = flatten(index - key, 43)
                plain_text += SPECIAL_CHARS[new_index]
            elif letter.isupper():
                index = ALPHABET.find(letter.upper())
                new_index = flatten(index - key, 27)
                plain_text += ALPHABET[new_index]
            else:
                index = alphabet.find(letter.lower())
                new_index = flatten(index - key, 27)
                plain_text += alphabet[new_index]
    
    return plain_text

def closer(letterFrequency, closestFrequencies, frequencies):
    a=0
    b=0
    for i in range(len(letterFrequency)):
        a = a + abs(letterFrequency[i] - closestFrequencies[i])
        b = b + + abs(letterFrequency[i] - frequencies[i])
    if(a>b):
        return True
    else:
        return False
    
def find_key2(cipher_text):
    letterFrequency = [12.53, 1.42, 4.68, 5.86, 13.68, 0.69, 1.01, 0.70, 6.25, 0.44, 0.02, 4.97, 3.15, 6.71, 0.31, 8.68, 2.51, 0.88, 6.87, 7.98, 4.63, 3.93, 0.90, 0.01, 0.22, 0.90, 0.52]
    modified_text = cipher_text
    for c in SPECIAL_CHARS:
        modified_text = modified_text.replace(c, '')
    
    
    allfrequencies = []
    for i in range(len(alphabet)):
        temp_text = decrypt2(modified_text, i)
        templist = []
        for j in range(len(alphabet)):
            templist.append( (temp_text.count(alphabet[j])/len(temp_text))*100)
        allfrequencies.append(templist)
    
    correctkey=0
    closestFrequencies = allfrequencies[0]
        
    for i in range(len(allfrequencies)):
        if(closer(letterFrequency, closestFrequencies, allfrequencies[i])==True):
            closestFrequencies = allfrequencies[i]
            correctkey = i
    
    return correctkey
    
            
         
    
def decrypt(cipher_text, key=None):

    if key is None:
        key = find_key_from_cipher(cipher_text)

    plain_text = ""
    for letter in cipher_text:
        if letter == ' ':
            plain_text += letter
            continue
        else:
            #Skipping special characters (incomplete solution)
            if letter in SPECIAL_CHARS:
                index = SPECIAL_CHARS.find(letter)
                new_index = flatten(index - key, 43)
                plain_text += SPECIAL_CHARS[new_index]
            elif letter.isupper():
                index = ALPHABET.find(letter.upper())
                new_index = flatten(index - key, 27)
                plain_text += ALPHABET[new_index]
            else:
                index = alphabet.find(letter.lower())
                new_index = flatten(index - key, 27)
                plain_text += alphabet[new_index]
    
    return plain_text

def flatten(number, size) :
    return number%size


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
    modified_text = modified_text.replace(' ', '')
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

