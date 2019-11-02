# Ancora Imparo.

from config import Config

from twilio.rest import Client

def send_twilio(phone, content):
	account_sid = Config.vars['twilio']['sid']
	auth_token = Config.vars['twilio']['token']
	client = Client(account_sid, auth_token)
	message = client.messages.create(
		body=content,
		from_=Config.vars['twilio']['no'],
		to=phone
	)
	return message

def config():
	return {
		'version':5.8,

		'gateways':{
			'twilio':send_twilio
		}
	}