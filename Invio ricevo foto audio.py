# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 19:14:03 2021

@author: peppi
"""

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
#
from telebot import types
#

TOKEN="###############################"

bot=telebot.TeleBot(TOKEN)



'''
i bot.message....
possono essere messi uno sotto laltro per porte utilizzare la stessa funzione

'''

#se il bot riceve /start o /help viene avviata questa funzione
@bot.message_handler(commands=['start','help'])
def send_welcom(message):
    bot.reply_to(message,' Ciao sono un bot appena creato, il mio padrone e Piko')
    
  

#pulsanti sulla chat  #############################################################################################
@bot.message_handler(commands=['pulsanti'])
def exchange_command(message):
    
     bot.send_message(message.chat.id, 'invio messaggio testuale', reply_markup=bottoneChat() )   
     
def bottoneChat():
    
    #creo bottoni
    bottoni=InlineKeyboardMarkup()
    bottoni.row(InlineKeyboardButton('Scritta sul bottone', callback_data='primo'))
    bottoni.row(InlineKeyboardButton('Si', callback_data='Si'),
                InlineKeyboardButton('No', callback_data='No'))
    return bottoni

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    if call.data == "Si":
        bot.answer_callback_query(call.id, "Answer is Yes")
    elif call.data == "No":
        bot.answer_callback_query(call.id, "Answer is No")
    elif call.data=='primo':
        bot.edit_message_text('forse',cid,mid)
#fine pulsanti sulla chat###########################################################################################        


#####################################
#per messagi scritti messaggi di testo
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    #print(message)   #per vedere da quanti campi e composto il messagio attivare questa riga
    if message.text=='Ciao':
        bot.reply_to(message,'Piacere di conoscerti')
    elif message.text=='Male':              #################################### Riconosce bottoni a posto della tastiera e cabia i bottoni
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Male1', 'Female1')
        markup.add('terzo')
        markup.add('quarto')##################################################################
        msg = bot.reply_to(message, 'What is your gender', reply_markup=markup)
    else:
        bot.reply_to(message,'Al momento non capisco cosa vuoi dire')
    

'''
content_types=["text", "sticker", "pinned_message", "photo", "audio"]

content_type can be one of the following strings: text, audio, document, photo, sticker, video, video_note, voice, 
location, contact, new_chat_members, left_chat_member, new_chat_title, new_chat_photo, delete_chat_photo,
group_chat_created, supergroup_chat_created, channel_chat_created, migrate_to_chat_id, migrate_from_chat_id,
pinned_message

'''

    
# Gestisce tutti i documenti inviati e i file audio (audio no note vocali pero)   
#per gli audio sono voice
@bot.message_handler(content_types=['document', 'audio','voice'])
def handle_docs_audio(message):
    print('hola')

@bot.message_handler(content_types=['photo'])
def handle_docs_audio(message):
    bot.reply_to(message,'Sei bello')

# bottoni al posto della tastiera ############################################################################
@bot.message_handler(content_types=['location'])
def handle_docs_audio(message):
    print(message)
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Male', 'Female')
    msg = bot.reply_to(message, 'What is your gender', reply_markup=markup) # con metodo forse
    #msg = bot.reply_to(message, 'What is your gender')
    
 
'''
per i bottoni al posto della tastiera,  sono visti come parole normali, mettere anche il pulsante torna indietro

'''

    
'''
#catena di messaggi
@bot.message_handler(commands=['go'])
def send_welcomGo(message):
    x=bot.reply_to(message,' quanti anni hai')
    bot.register_next_step_handler(x, askAge)


def askAge(message):
    text=message.text
    
    if not text.isdigit():
        msg=bot.send_message(message, 'prova non so catena messaggi')
        bot.register_next_step_handler(msg, askAge)
    
    return msg
'''        

bot.polling()  #obbligatorio per avviare il bot










