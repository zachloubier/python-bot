import os
import sys
import json
from flask import Flask, request
app = Flask(__name__)


@app.route('/', methods=['GET'])
def verify():
	if request.args.get('hub.mode') == 'subscribe' and request.args.get('hub.challenge'):
		if not request.args.get('hub.verify_token') == os.environ.get('VERIFY_TOKEN'):
			return 'Verification token mismatch', 403
		return request.args.get('hub.challenge'), 200

	return 'Got your message!', 200
