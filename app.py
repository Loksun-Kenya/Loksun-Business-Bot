from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "PASTE_YOUR_LONG_TOKEN_EXACTLY_HERE"

@app.route('/')
def home():
    return "Bot is running!"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():

    if request.method == 'GET':
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if token == VERIFY_TOKEN:
            return challenge
        return "Verification token mismatch", 403

    if request.method == 'POST':
        return "EVENT_RECEIVED", 200
