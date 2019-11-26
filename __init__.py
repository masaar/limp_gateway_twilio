# Ancora Imparo.

from config import Config

from typing import TypedDict
from twilio.rest import Client

def twilio_gateway(
			phone: str,
			content: str,
			twilio_auth: TypedDict('GATEWAY_TWILIO_AUTH', sid=str, token=str, no=str)=None
		):
	if not twilio_auth:
		twilio_auth = Config.vars['twilio']
	account_sid = twilio_auth['sid']
	auth_token = twilio_auth['token']
	client = Client(account_sid, auth_token)
	message = client.messages.create(
		body=content,
		from_=twilio_auth['no'],
		to=phone
	)
	return message

def config():
	return {
		'version':5.8,

		'gateways':{
			'twilio':twilio_gateway
		}
	}