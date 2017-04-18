from flask import Flask
app = Flask(__name__)


page_token = 'EAAF3iaUxWAIBAMJ06XDwFZA0gZCQkTZC0cqudDzEUZBxLcezyfPC2F0Mz1SEaLSjb0guZCrtoExae0pQj7BqdoMqS060RkcdyG3VVgJ80Tjnl84xtER7WIKXLjie4udr7WpSyIG6uYh43t8sd8E678PQnHZC3evn1OpzKPlgvZCAQZDZD'
app_id = '412908042409986'


@app.route('/')
def receive_message():
	return 'Got your message!'
