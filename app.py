import os
from twilio.rest import Client

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to=os.getenv('TO_PHONE_NUMBER'),
                        from_=os.getenv('FROM_PHONE_NUMBER')
                    )

print(call.sid)
