from flask import Flask
from mpesa import get_access_token, lipa_na_mpesa, mpesa_callback

app = Flask(__name__)

# Routes for Mpesa API
app.add_url_rule('/get_token', 'get_token', get_access_token)
app.add_url_rule('/stk_push', 'lipa_na_mpesa', lipa_na_mpesa, methods=['POST'])
app.add_url_rule('/callback', 'mpesa_callback', mpesa_callback, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)
