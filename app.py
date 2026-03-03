import os
from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "LoksunBusinessBot"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # GET part for verification stays as is
    if request.method == "GET":
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if token == VERIFY_TOKEN:
            return challenge
        return "Verification token mismatch", 403

    # POST part for incoming messages
    if request.method == "POST":
        # THIS IS WHAT WE ADD
        data = request.get_json()
        print("Incoming webhook:", data)  # <-- This prints the full message to your Render logs
        return "EVENT_RECEIVED", 200

