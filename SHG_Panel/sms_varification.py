import random
from twilio.rest import *


def SmsVarification(mobileNumber):
			otp = random.randint(10000,99999)
			
			
			mob = mobileNumber
			print(otp)

			account_sid = 'AC3f932979df66868342386abba349922f'
			auth_token = '43659b068bc654658e36b82a0be231ca'
			client = Client(account_sid, auth_token)


			message = client.messages.create(
		            body = 'Your otp is -' + str(otp),
		            from_ = '+12058517914',
		            to = '+918839654349')


			print(message.sid)
			return message.sid , otp
