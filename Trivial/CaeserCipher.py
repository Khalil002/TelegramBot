import enchant
import collections

characters  = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~áéíóú" 
characters += '"'
special_characters = characters[54:101]
letters_by_frequency = "EAOSRNIDLCTUMPBGVYQHFZJÑXKW"

#Recibe el codigo a encriptar y el shift que le va a aplicar al texto y se lo manda a la funcion moveText()
def encrypt(input_text, shift):
    return moveText(input_text, shift)

#Recibe el mensaje a desencriptar y calcula el shift necesario comparando todos los shifts possibles
def decrypt(input_text):
    d = enchant.Dict("es_CO")
    
    #Se eliminan los caracteres especiales debido a que no podemos revisar si son palabras
    filtered_text = input_text.upper()
    for sc in special_characters:
        filtered_text = filtered_text.replace(sc, '')
    most_common_letter = collections.Counter(filtered_text.replace(' ', '')).most_common(1)[0][0]
    
    #Se busca el shift que nos de la mayor cantidad de palabras correctamente decriptadas
    max=0
    output_text=""
    for letter in letters_by_frequency:
        shift= characters.find(most_common_letter)-characters.find(letter)
        text = moveText(input_text, -1*shift)
        words = text.split()
        
        count=0
        for word in words:
            if(d.check(word)):
                count+=1
        
        if(max<count):
            max=count
            output_text=text
            
    return output_text
        
#Esta es la funcion que se encarga de mover cada carácter del texto por el shift
def moveText(input_text, shift):
    output_text = ""
    for caracter in input_text:
        #En caso de que el carácter sea el espacio, se salta
        if(caracter == ' '):
            output_text+=caracter
        else:
            index = characters.find(caracter)
            new_index = new_index = flatten(index + shift) 
            output_text+= characters[new_index]
    
    return output_text

#Esta funcion se encarga de mantener el shift dentro del tamaño de la lista de caracteres
def flatten(shift):
    return shift - (len(characters)*(shift//len(characters)))
