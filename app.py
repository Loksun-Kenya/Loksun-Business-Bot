import os
from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "LoksunBusinessBot"

@app.route('/')
def home():
    return "Bot is running!"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == "GET":
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if token == VERIFY_TOKEN:
            return challenge
        return "Verification token mismatch", 403

    if request.method == "POST":
        return "EVENT_RECEIVED", 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
