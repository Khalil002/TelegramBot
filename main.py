from bs4 import SoupStrainer
import Constants as keys
from telegram.ext import *
import CaeserCipher as cc

cipher = False
decipher = False
text = ""
index = -1
shift = 0

#El comando que se activa con /start, lo que hace es saludar al usuario
def start_command(update, context):
    update.message.reply_text('¡Hola! Soy el CaeserCipherBot, puedo cifrar y descifrar códigos cesar. Si necesitas ayuda, escribe el comando /ayuda.')

#El comando que se activa con /ayuda, lo que hace es mostrar lo que el bot puede hacer
def help_command(update, context):
    update.message.reply_text('/cifrar: Este comando recibe el texto que deseas cifrar y el número de desplazamiento que vas a utilizar.\n/descifrar: Este comando recibe el texto cifrado y te lo descifra.')

#El comando que se activa con /cifrar, lo que hace es encender la señal de que se va a encriptar el siguiente mensaje
def cipher_command(update, context):
    global cipher, index
    cipher = True
    index = 0
    update.message.reply_text('Escriba el texto que desea cifrar:')

#El comando que se activa con /descifrar, lo que hace es encender la señal de que se va a desencriptar el siguiente mensaje 
def decipher_command(update, context):
    global decipher
    decipher = True
    update.message.reply_text('Escriba el texto que desea descifrar:')

#Aqui se reciben los mensajes ordinarios del usuario
def handle_message(update, context):
    global cipher, decipher, index, text, shift
    msg = str(update.message.text)
    
    if(cipher):
        #En caso de que la señal de cifrar esta activa, se empieza el proceso para recolectar el texto y el shift del usuario
        if(index==0):
            text = msg
            print("El mensaje resibido es: "+text)
            update.message.reply_text('Escriba el numero de desplazamiento:')
            index = 1
        elif(index==1):
            shift = int(msg)
            update.message.reply_text('Texto cifrado: ')
            update.message.reply_text(cc.encrypt(text, shift))
            index = -1
            cipher = False
    elif(decipher):
        #En caso de que la señal de descifrar esta activa, se le descifra al usuario el texto que escribo
        update.message.reply_text('Texto descifrado: ')
        update.message.reply_text(cc.decrypt(msg))
        decipher = False
    else:
        #Si ninguna señal esta activa el bot simplemente no sabe que hacer asique le pide al usuario que escriba un comando de la lista de ayuda
        update.message.reply_text('Lo siento, no entendí. Escribe el comando /ayuda para más información.')
        
#Esta funcion es llamada en caso de que suceda un error en el bot y imprime dicho error
def error(update, context):
    print(f"Update {update} caused error  {context.error}")

#Aqui es donde se crea el bot y se le dice como manejar cada caso
def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher
    
    #Manejo de comandos
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("ayuda", help_command))
    dp.add_handler(CommandHandler("cifrar", cipher_command))
    dp.add_handler(CommandHandler("descifrar", decipher_command))
    
    #Manejo de mensajes
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    
    #Manejo de errores
    dp.add_error_handler(error)
    
    #Empezar a sondear
    updater.start_polling()
    
    #Esperar respuesta
    updater.idle()

#Empezar el bot
print('Bot started...')
main()
