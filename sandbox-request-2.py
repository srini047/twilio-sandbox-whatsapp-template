from twilio.rest import Client 
 
account_sid = 'AC0d725340d8bb849879c71beb31b2a382' 
auth_token = '' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Hello! How can I help you with today.',      
                              to='whatsapp:+916385685916' 
                          ) 
 
print(message.sid)
