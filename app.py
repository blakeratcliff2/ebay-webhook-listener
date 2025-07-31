from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Set your token (this must match what you input on eBay)
VERIFICATION_TOKEN = "ai-ebay-listener-2025-token-for-marketplace-verify"

@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        challenge = request.args.get('challenge_code')
        verify_token = request.args.get('verify_token')
        if verify_token == VERIFICATION_TOKEN:
            return jsonify({"challengeResponse": challenge}), 200
        else:
            return "Invalid verification token", 403

    if request.method == 'POST':
        data = request.json
        print("Incoming webhook:", data)
        return "Received", 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
