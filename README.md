# LIMP Gateway for Twilio
This repo is a [LIMP](https://github.com/masaar/limp) [Package](https://github.com/masaar/limp-docs/blob/APIv5.8/api/package.md) for the sole purpose of integrating [Twilio SMS](https://www.twilio.com/sms) into LIMP apps using [LIMP Gateways](https://github.com/masaar/limp-docs/blob/APIv5.8/api/gateways.md).

## How-to
1. Clone this repo into your LIMP `modules` folder.
2. Add following to your app package config:
```python
'vars':{
	'twilio':{
		'sid':'YOUR_TWILIO_SID_HERE',
		'token':'YOUR_TWILIO_TOKEN_HERE',
		'no':'YOUR_TWILIO_PHONE_HERE'
	}
}
```
3. Twilio gateway requires following args:
   1. `phone`: Target phone number using international format with prefixed `+`. Type `str`.
   2. `content`: Message body. Type `str`.
4. Twilio gateway accepts optional arg, namely `twilio_auth`, replicating `twilio` value in `vars Config Attr` for dynamic Twilio API credentials.
5. Use Twilio gateway using LIMP Gateway Controller:
```python
from gateway import Gateway

Gateway.send(gateway='twilio', phone=phone, content=content)
```