# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import telebot

API_TOKEN = '###########################'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    #Messaggio appena si avvia il bot
    bot.reply_to(message, """\
Ciao sono un bot creato da Piko e devo ancora imparare\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    
    if message.text=='Ciao':  #se il messagio ricevuto e ciao
        bot.reply_to(message,'Ciao come stai?') #il bot risponde cosi
    elif message.text=='Bene':
        bot.reply_to(message,'mi fa piacere')
    
    else:
        bot.reply_to(message,'non ho capito')
    
     


bot.polling()
