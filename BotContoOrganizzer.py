import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types
import csv
from datetime import datetime




PATH="#########################"
API_TOKEN = "##########################################################"

conto="conto"
ricordami="Ricordami il giorno.."
SALDO="Saldo"
LISTAMOVIMENTI="ListaMovimenti"
ri=0
ricordo=""
data=""

dataformat="%Y-%m-%d"

bot = telebot.TeleBot(API_TOKEN)
dataVecchia=["2020","08"]
somma=0


def controllo(message):
    
    if(message.chat.id==@@@@@@ and message.chat.first_name=="@@@@@@@@@@" and message.chat.username=="@@@@@@@@@@@@@@"):
        print("sei tu")
        return True
    else:
        return False


######################################################################################################
########################### gestione bottoni tastiera ################################################
#ascolta messaggi di testo 
# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    
    if(controllo(message)==True):
        
        global dataVecchia,fl
        '''
        dataDiOggi=dataG=datetime.today().strftime('%Y-%m-%d').split("-")
        #print(dataVecchia, "  ",dataDiOggi)
        if(int(dataVecchia[0])!=int(dataDiOggi[0]) and int(dataVecchia[1])!=int(dataDiOggi[1])):
            #print("ok")
            dataVecchia=dataDiOggi
            verificaricordi(message)
        
        
        
        
        global ri
        if(message.text==ricordami or ri>0):
            
            ri+=1
            ricorda(message)
            
        '''  
        if (message.text==conto):
            #bot.send_message(message.chat.id,'Cosa devi fare ', reply_markup=bottoniDue())
            fl=0
            tipologiaConto(message)
            
            
        elif(message.text=="Chat"):
            listaMovimenti(message)
            
        elif(message.text=="Documento"):    ###############################################invio documento
        
            if(fl==1):
                bot.send_document(message.chat.id, open(PATH+"Banca.csv","r") )
            else:
        
                bot.send_document(message.chat.id, open(PATH+"file.csv","r") )
            menuPrincipale(message)
            
        elif(message.text=="Mio"):
            fl=0
            bot.send_message(message.chat.id,'Cosa devi fare ', reply_markup=bottoniDue())
            menuPrincipale(message)
            
        elif(message.text=="Banca"):
            #print("banca")
            fl=1
            bot.send_message(message.chat.id,'Cosa devi fare ', reply_markup=bottoniDue())
            menuPrincipale(message)
            
            
        else:
            
            menuPrincipale(message)
        
            
            
             
        
    else:
        bot.reply_to(message,"accesso non autorizzato, non puoi comunicare con questo bot")
        
        
        
        
def menuPrincipale(message):                                           ############################ aggiungere controllo
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            #markup.add('Male', 'Female')
            markup.add(conto)
            markup.add(ricordami)
            bot.reply_to(message,"Ciao",reply_markup=markup) 
            
            
  
            
'''  
def verificaricordi(message):                                        ############################ aggiungere controllo
    print("okkkkkkkkkkkkkkkk")
    with open(PATH+"Ricordo.csv","r") as file:
        #scrivi=csv.reader(file) 
       
        for line in file.readlines():
            array = line.split(',')
            first_item = array[0]
            second_item=array[1]
            #print(first_item)
            print(first_item)
            print(second_item)
            bb=first_item.split("-")
            print(bb)
            dataG=datetime.today().strftime('%Y-%m-%d').split("-")
            print(dataG)
            
            if(bb[0]==dataG[0] and bb[1]==dataG[1]):
                bot.reply_to(message,"ricordati "+str(second_item)+" in data "+str(first_item))
                
   
    
######################################################### settaggio di ricorda  ######
def ricorda(message):
    if(controllo(message)==True):
        global ri,ricordo,data
        if(ri==1):
            bot.reply_to(message,"Cosa per annullare /annulla")
        if (ri==2):
            ricordo=message.text
            print(message.text)
            bot.reply_to(message, "che giorno 'anno-mese-giorno'")
        if(ri==3):
            try:
                data=message.text
                bb=datetime.strptime(data, dataformat)
                print(bb)
                print(message.text)
                print(ricordo,'  ', data)
                ri=0
                bot.reply_to(message,"ok")
                menuPrincipale(message)
                
                with open(PATH+"Ricordo.csv","a") as file:
                   scrivi=csv.writer(file) 
                   
                   scrivi.writerow([bb,ricordo])
                  
                
            except ValueError:
                
                ri=0
                bot.reply_to(message,"errore inserimento data riprova tutto")
                menuPrincipale(message)
            
    else:
        bot.reply_to(message,"accesso non autorizzato, non puoi comunicare con questo bot") 
        
        
'''

'''
################################################################################################
                                CONTO
###############################################################################################

'''


def tipologiaConto(message):
    
    if(controllo(message)==True):
    
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Banca', 'Mio')
            bot.reply_to(message,"Quale conto",reply_markup=markup) 
    else:
        bot.reply_to(message,"accesso non autorizzato, non puoi comunicare con questo bot") 

        
###########################################################################################################################
####################################################### Bottoni a schermo  ################################################    
######################################à AGGIUNGI E SOTTRAI I SOLDI##########################################################
def bottoniDue():
    bottoni=InlineKeyboardMarkup()
    bottoni.row(InlineKeyboardButton('Aggiungi',callback_data='aggiungi'))
    bottoni.row(InlineKeyboardButton('Sottrai',callback_data='sottrai'))    
    bottoni.row(InlineKeyboardButton('Saldo',callback_data='saldo'),InlineKeyboardButton('ListaMovimenti',callback_data='ListaMovimenti'))    
    bottoni.row(InlineKeyboardButton('Statistica',callback_data='statistica'))    
    return bottoni



@bot.callback_query_handler(func=lambda call: True)   #####################################  callback
def callback_query(call):
     #print('hola')
    
     
     if call.data=='aggiungi':
            mes=bot.reply_to(call.message,'Somma da aggiungere')
            bot.register_next_step_handler(mes, aggiungi)
            
            
            
        
            
     elif call.data=='sottrai':
         mes=bot.reply_to(call.message,'Somma da sottrare')
         bot.register_next_step_handler(mes, sottrai)
         
     elif call.data=="saldo":
         bot.reply_to(call.message,"totale: "+ str(totaleSoldi()))
         
     elif call.data=="ListaMovimenti":
         
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Chat', 'Documento')
            bot.reply_to(call.message,"Scegli",reply_markup=markup)
            
     elif call.data=="statistica":
         #print("ciao amico okok")
         #statisticaFun(call)
         bot.reply_to(call.message,statisticaFun()+"\nTotale: "+str(totaleSoldi()))
         
         
        
##########################################################################################################         
         
#sottrazione dei soldi
def sottrai(message):
    if(controllo(message)==True):
        global somma
        somma=int(message.text)
        mes=bot.reply_to(message,'Casuale')
        bot.register_next_step_handler(mes, casualeSot)
    else:
        bot.reply_to(message,"accesso non autorizzato, non puoi comunicare con questo bot")
    
#casuale sottrazione soldi
def casualeSot(message):
    if(controllo(message)==True):
        data=datetime.today().strftime('%Y-%m-%d')
        #print(data)   #stampa la data
        scriviCsv(somma, message.text, data,"-")
        bot.reply_to(message,"totale: "+ str(totaleSoldi()))
    else:
        bot.reply_to(message,"accesso non autorizzato, non puoi comunicare con questo bot")

#aggiunge i soldi
def aggiungi(message):
    if(controllo(message)==True):
        global somma
        somma=int(message.text)
        mes=bot.reply_to(message,'Casuale')
        bot.register_next_step_handler(mes, casuale)
    else:
        bot.reply_to(message,"accesso non autorizzato, non puoi comunicare con questo bot")
    
#casuale per aggiunta soldi
def casuale(message):
    if(controllo(message)==True):
        data=datetime.today().strftime('%Y-%m-%d')
        #print(data)   #stampa la data
        scriviCsv(somma, message.text, data,"+")
        bot.reply_to(message,"totale: "+ str(totaleSoldi()))
    else:
        bot.reply_to(message,"accesso non autorizzato, non puoi comunicare con questo bot")
        
####################################################################################################################################
###################################################################################################################################
################################### LAORAZIONE NEL CSV #############################################################################


#scrivi nel csv
def scriviCsv(soldi,casuale,data,segno):
    
    if(fl==1):
        
         with open(PATH+"Banca.csv","a") as file:
           scrivi=csv.writer(file) 
           if segno=="+":
               scrivi.writerow([soldi,"£",casuale,data])
           else:
                scrivi.writerow([soldi*(-1),"£",casuale,data])
    
    else:
    
        with open(PATH+"file.csv","a") as file:
           scrivi=csv.writer(file) 
           if segno=="+":
               scrivi.writerow([soldi,"£",casuale,data])
           else:
                scrivi.writerow([soldi*(-1),"£",casuale,data])
            

#ritorna solo il totale dei soldi
def totaleSoldi():
    tot=0
    
    if(fl==1):
        with open(PATH+"Banca.csv","r") as file:
            #scrivi=csv.reader(file) 
           
            for line in file.readlines():
                array = line.split(',')
                first_item = array[0]
                #print(first_item)
                tot=tot+int(first_item)
        
    else:
    
        with open(PATH+"file.csv","r") as file:
            #scrivi=csv.reader(file) 
           
            for line in file.readlines():
                array = line.split(',')
                first_item = array[0]
                #print(first_item)
                tot=tot+int(first_item)
    return tot
    

def listaMovimenti(call):
    
     tot=[]
     
     if(fl==1):
         
        with open(PATH+"Banca.csv","r") as file:
         
         for line in file.readlines():
            array = line.split(',')
            first_item = array
            #print(first_item)
            tot.append(first_item)
            
         ############################################à METTERE UN COMTROLLO SU TOT SE SI VOGLIONO LE ULTIME != MOVIMENTI
         if(len(tot)>15):
             tot=tot[-15:]
             
         stringa=""
         #print(len(tot))
         for i in tot:
             stringa=stringa+str(i)+"\n"
             
         #print(stringa)
         bot.reply_to(call,stringa+"\nTotale: "+str(totaleSoldi()))
         menuPrincipale(call)
         
     else:
     
         with open(PATH+"file.csv","r") as file:
             
             for line in file.readlines():
                array = line.split(',')
                first_item = array
                #print(first_item)
                tot.append(first_item)
                
             ############################################à METTERE UN COMTROLLO SU TOT SE SI VOGLIONO LE ULTIME != MOVIMENTI
             if(len(tot)>15):
                 tot=tot[-15:]
                 
             stringa=""
             #print(len(tot))
             for i in tot:
                 stringa=stringa+str(i)+"\n"
                 
             #print(stringa)
             bot.reply_to(call,stringa+"\nTotale: "+str(totaleSoldi()))
             menuPrincipale(call)
        
            
     

def statisticaFun():
    
    lista=[]
    stringa="Statistica:\n"
    num=0
    
    
    if(fl==1):
    
        with open(PATH+"Banca.csv","r") as file:
             
             for line in file.readlines():
                array = line.split(',')
                first_item = array
                
                
                if(int(first_item[0])<0):
                    lista.append(first_item)
        #print("lista ee eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee ", lista)  
             
        i=0
        while(i<len(lista)):
                 j=i+1
                 num=int(lista[i][0])
                 while(j<len(lista)):
                     if (lista[i][2]==lista[j][2]):
                         num+=int(lista[j][0])
                         lista.pop(j)
                     j+=1
                 stringa+=lista[i][2]+"  "+str(num)+"\n"    
                 i+=1
        
    else:
    
        with open(PATH+"file.csv","r") as file:
             
             for line in file.readlines():
                array = line.split(',')
                first_item = array
                
                
                if(int(first_item[0])<0):
                    lista.append(first_item)
        #print("lista ee eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee ", lista)  
             
        i=0
        while(i<len(lista)):
                 j=i+1
                 num=int(lista[i][0])
                 while(j<len(lista)):
                     if (lista[i][2]==lista[j][2]):
                         num+=int(lista[j][0])
                         lista.pop(j)
                     j+=1
                 stringa+=lista[i][2]+"  "+str(num)+"\n"    
                 i+=1
                 
    #print(lista[i-1])
    #print(stringa)
    return stringa
                
                
                
                
     
    

'''
###############################################################################################################################
################################ BOTTONI NELLA CHAT ########################################################################
#i bottoni vengono visti come messagi di testo normali 
    
@bot.message_handler(commands=['goo'])
def handle_docs_audio(message):
    print(message)
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    #markup.add('Male', 'Female')
    markup.add('Conto22')
    markup.add('Ricormali giorno..')
        
    msg = bot.reply_to(message,"OK un Attimo",reply_markup=markup) # con metodo forse
    #msg = bot.reply_to(message, 'What is your gender')
    
        
    

#################################################################################################################
################################################################################################################
'''


bot.polling()  #obbligatorio per avviare il bot

