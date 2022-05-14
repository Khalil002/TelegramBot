from bs4 import SoupStrainer
import Constants as keys
from telegram.ext import *
import CaeserCipher as cc

cipher = False
decipher = False
text = ""
index = -1
shift = 0

def start_command(update, context):
    update.message.reply_text('¡Hola! Soy el CaeserCipherBot, puedo cifrar y descifrar códigos cesar. Si necesitas ayuda, escribe el comando /ayuda.')
    
def help_command(update, context):
    update.message.reply_text('/cifrar: Este comando recibe el texto que deseas cifrar y el número de desplazamiento que vas a utilizar.\n/descifrar: Este comando recibe el texto cifrado y te lo descifra.')
    
def cipher_command(update, context):
    global cipher, index
    cipher = True
    index = 0
    update.message.reply_text('Escriba el texto que desea cifrar:')
    
def decipher_command(update, context):
    global decipher
    decipher = True
    update.message.reply_text('Escriba el texto que desea descifrar:')

    
def handle_message(update, context):
    global cipher, decipher, index, text, shift
    msg = str(update.message.text)
    if(cipher):
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
        update.message.reply_text('Texto descifrado: ')
        texta = cc.decrypt(msg)
        textb = cc.decrypt2(msg)
        print('1: ',texta)
        print('2: ',textb)
        update.message.reply_text(cc.decrypt(msg))
        decipher = False
    else:
        update.message.reply_text('Lo siento, no entendí. Escribe el comando /ayuda para más información.')
        
    
def error(update, context):
    print(f"Update {update} caused error  {context.error}")
    
def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher
    
    #Command handling
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("ayuda", help_command))
    dp.add_handler(CommandHandler("cifrar", cipher_command))
    dp.add_handler(CommandHandler("descifrar", decipher_command))
    
    #Message Handling
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    
    #Error handling
    dp.add_error_handler(error)
    
    #Start polling
    updater.start_polling()
    
    #Wait for response
    updater.idle()

#Start bot

print('Bot started...')
main()
