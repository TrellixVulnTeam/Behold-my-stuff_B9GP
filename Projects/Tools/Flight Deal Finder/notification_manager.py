from twilio.rest import Client

TWILIO_SID = #Twilio Acc
TWILIO_AUTH_TOKEN = #Twilio token
TWILIO_VIRTUAL_NUMBER = #Twilio virtual number
TWILIO_VERIFIED_NUMBER = #Twilio verified number


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
