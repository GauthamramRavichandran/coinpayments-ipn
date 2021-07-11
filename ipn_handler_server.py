from flask import Flask, request
import hmac
import hashlib
from urllib.parse import urlencode

app = Flask(__name__)

SECRET = 'itsnotmine'
@app.route("/ipn/", methods = ["POST"])
def receive_ipn():
	received_hmac = request.headers['Hmac'])
	generated_hmac = hmac.new(key = bytearray(SECRET, 'utf-8'), 
                              msg = urlencode(request.form.to_dict()).encode('ascii'), # raw POST data will be passed here
                              digestmod = hashlib.sha512).hexdigest()
	if received_hmac == generated_hmac:
   	  pass  # do your thing here, notify user, save txn in DB ...
  	else:
    	  pass # ignore, since it's not the right one


if __name__ == "__main__":
	app.run()
