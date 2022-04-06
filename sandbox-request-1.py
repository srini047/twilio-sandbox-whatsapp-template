from twilio.rest import Client
import os
 
account_sid = 'AC0d725340d8bb849879c71beb31b2a382' 
auth_token = ''
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Your Yummy Cupcakes Company order of 1 dozen frosted cupcakes has shipped and should be delivered on July 10, 2019. Details: http://www.yummycupcakes.com/',      
                              to='whatsapp:+916385685916' 
                          ) 
 
print(message.sid)
