import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import smtplib #per inviare email


import random
import string
import mysql.connector

TOKEN='#################'

bot=telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start'])
def avvio(message):
    bot.reply_to(message, 'Ciao, sono un bot Stupido creato da Piko')
    print(message.from_user.id)
    controlloRegistrazione(message,0)
    

########################################  REGISTRAZIONE passi obbligati 
@bot.message_handler(commands=['registra'])
def registrazione(message):
    fl=False
    fl=controlloRegistrazione(message,1)
    
    if fl==False:
        bot.send_message(message.chat.id,'sei maggiorenne',reply_markup=bottoniChat())
    else:
        bot.reply_to(message,'sei gia registrato')


@bot.message_handler(commands=['go'])
def cosaPossofare(message):
    
    bot.send_message(message.chat.id,'ecco cosa puoi fare: ', reply_markup=bottoniDue())
   
###############################################################################

def bottoniDue():
    bottoni=InlineKeyboardMarkup()
    bottoni.row(InlineKeyboardButton('cerca film',callback_data='film'))
    bottoni.row(InlineKeyboardButton('cerca serie',callback_data='serie'))
    bottoni.row(InlineKeyboardButton('scarica canzone',callback_data='canzone'))
    
    return bottoni

def codiceConferma(message):
    try:
        global email
        email=message.text
        print('email ', email)
        global codiceSicurezza
        codiceSicurezza=invioEmail(email, message)
        print('\n\ncondice di verifica ',codiceSicurezza,'\n\n')
        mes=bot.reply_to(message,'inserisci il codice di conferma inviato alla tua email')
        bot.register_next_step_handler(mes, codiceConferma2)
    except:
        print('error1')
        bot.reply_to(mes,'ci dispiace si e verificato un errore')
        
        
def codiceConferma2(message):
    text=message.text
    print('non sooo,   ', codiceSicurezza)
    if(text==codiceSicurezza):
        registraDentroDatabase(message)
        bot.reply_to(message,'registrazione completata,buon divertimento')
        bot.send_message(message.chat.id,'per sapperne di piu clicca o dicita"/go"')#################################################
    else:
        print('error2')
        bot.reply_to(message,'codice errato, rieseguire tutta la procedura "/registra"')
    

def bottoniChat():
    print('heiiii')
    bottoni=InlineKeyboardMarkup()
    print('heiiii111')
    bottoni.row(InlineKeyboardButton('Si', callback_data='Si'),
                InlineKeyboardButton('No', callback_data='No'))
    print('heiiii333')
    return bottoni

@bot.callback_query_handler(func=lambda call: True)   #####################################  callback
def callback_query(call):
     print('hola')
     global maggiorennefl 
     maggiorennefl=False
     cid = call.message.chat.id
     mid = call.message.message_id
     if call.data=='Si':
            mes=bot.reply_to(call.message,'ok ti puoi registrare allora\nInserisci indirizzo email')
            bot.register_next_step_handler(mes, codiceConferma)
        
            
     elif call.data=='No':
        bot.reply_to(call.message,'Mi dispiace ma non puoi usare il bot')
        
     elif call.data=='film':
         print('film')
     else:
        print('ciao')

'''
@bot.callback_query_handler(func=lambda call: True)   #####################################  callback
def callback_query_Go(call):
'''        
################################################################# FUNZIONI di SERVIZIO #################

##############################################################################  EMAIL ########################
def invioEmail(testo,message):
    oggetto = "Subject: Urgente! da leggere subito!\n\n"
    codiceSicurezza=codiceDainviare()
    print('invio email funzione   ', codiceSicurezza,  'speriamo')
    contenuto = codiceSicurezza
    messaggio = oggetto + contenuto
    email = smtplib.SMTP("smtp.gmail.com", 587)
    email.ehlo()
    email.starttls()
    email.login("escofrancesco55@gmail.com", "cagnazzi123123")
    try:
        email.sendmail("escofrancesco55@gmail.com",testo, messaggio.encode('utf-8'))
    except:
       bot.reply_to(message,'Si è verificato un errore riprova di nuovo')
       
    email.quit()
    return codiceSicurezza
    

def codiceDainviare():
    stringa=string.ascii_letters
    
    for i in range(5):
        codiceSicurezza=random.choice(stringa)
    print('codice funzione ',codiceSicurezza, '   codice funzione')
    return codiceSicurezza
    
########################################################################## MYSQL #############################
########################################CONTROLLO REGISTRAZIONE
def controlloRegistrazione(message,x):
    
    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='123123123',
        database='telegram'
        )
    
    mycursor=mydb.cursor()
    
    univoco=message.from_user.id
    query='select * from utenti where id='+str(univoco)
    mycursor.execute(query)
    risultato=mycursor.fetchall()
    print(risultato)
    
    if(len(risultato)==0):
        if x==1:
            bot.reply_to(message, 'Non sei ancora registrato, provediamo alla registrazione')
            return False
        else:
            bot.reply_to(message, 'Non sei ancora registrato, per registrarti scrivi "/registra"')
            return False
    else:
        return True
    
    
    
    mydb.close()

############################### Registrazione

def registraDentroDatabase(message):
    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='123123123',
        database='telegram'
        )
    
    mycursor=mydb.cursor()
    
    query='insert into utenti value ('+str(message.from_user.id)+',"'+str(email)+'","")'
    mycursor.execute(query)
    mydb.commit()

    mydb.close()
    

############

bot.polling()  #obbligatorio per avviare il bot



