from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "EAALVZAMAS3KMBQ6NMwlSDBAVNwkZBh3sXG761PDU1VckRdkgWcWhkGJsSCLJCGBlpLt2X3EK0ROoleO78mHtIgDqMveEIHRZAlbsn5yLHJrGwyXtY8pdvR3ZByTSAEjGvLpMVDkwIFiAui2D1TbcfYf7ZC12M4EYGfD1gboXGqXWTj1FyO5FzvP8CeM5qZAVF69o2mOTPP81562FLZC124n1YthD72i7oXwTuwyQynEQvtYQc8xhkj1vzZBxFdBQWwh1GO8Kl5qaMZAXUZCQUk4lLtv5rDuwREC43pzAZDZD"

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
