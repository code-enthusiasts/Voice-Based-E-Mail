from text_speech import *
from send import *
from listmessages import *



while True :


 text_to_speech('say 1 to send a message !')
 text_to_speech('say 2 to receive messages !')
 text_to_speech('say 3 to close the application !')

 first_response=speech_to_text()

 if first_response == '1' :
  send_message()

 elif first_response == '2' or first_response == 'tu' or first_response == 'two' or first_response == 'Tu' or first_response == 'to' or first_response == 'To' :
  text_to_speech('say 1 for top ten messages')
  text_to_speech('say 2 to search for a sender')
  receive_response=speech_to_text()
  if receive_response == '1' :
   get_message_list()
  if receive_response == '2' or receive_response == 'Tu' or receive_response == 'tu' or receive_response == 'two' or receive_response == 'To' or receive_response == 'to':
   text_to_speech('Say the E-Mail of the sender!')
   email=speech_to_text()
   words=email.split()
   modified_mail=str()
   for word in words:
     if word == 'underscore':
       modified_mail=modified_mail+'_'
     elif word == 'dot':
       modified_mail=modified_mail+'.'
     else:
       modified_mail=modified_mail+word

   modified_mail=modified_mail.lower()
   #query=speech_to_text()
   searched_message(modified_mail)
 elif first_response == '3':
  exit()
 else:
  text_to_speech('Sorry you were not clear with your vocals !')
  continue
  
 


 

