from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "LoksunVerify123"

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if token == VERIFY_TOKEN:
            return challenge
        return "Verification failed"

    if request.method == "POST":
        data = request.json
        print(data)
        return "OK", 200

@app.route("/")
def home():
    return "Bot is running!"

from flask import Flask, request
import os

app = Flask(__name__)

VERIFY_TOKEN = "LoksunVerify123"

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if token == VERIFY_TOKEN:
            return challenge
        return "Verification failed"

    if request.method == "POST":
        data = request.json
        print(data)
        return "OK", 200

@app.route("/")
def home():
    return "Bot is running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
