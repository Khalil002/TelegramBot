import enchant
import collections

characters  = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóú0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~" 
characters += '"'
special_characters = characters[59:101]
characters_by_frequency = "eEaAoOsSnRrNiIlDdLuCtTcUmMpPqByGbVhYvQgHjFfZzJñÑkXwKxWáéíóú"+special_characters

#Recibe el codigo a encriptar y el shift que le va a aplicar al texto y se lo manda a la funcion moveText()
def encrypt(input_text, shift):
    return moveText(input_text, shift)

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
    return shift%len(characters)

#Recibe el mensaje a desencriptar y calcula el shift necesario comparando todos los shifts possibles
def decrypt(input_text):
    d = enchant.Dict("es_CO")
    
    most_common_letter = collections.Counter(input_text.replace(' ', '')).most_common(1)[0][0]

    #Se busca el shift que nos de la mayor cantidad de palabras correctamente decriptadas
    max=0
    output_text=""
    for letter in characters_by_frequency:
        shift= characters.find(most_common_letter)-characters.find(letter)
        
        #Se eliminan los caracteres especiales debido a que no podemos revisar si son palabras        
        text = moveText(input_text, -1*shift)
        for sc in special_characters:
            text = text.replace(sc, '')
        words = text.split()
        
        count=0
        for word in words:
            if(d.check(word)  and len(word)>1):
                count+=1
                
        if(max<count):
            max=count
            output_text=moveText(input_text, -1*shift)

    return output_text
        



