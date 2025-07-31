from flask import Flask, request, jsonify

app = Flask(__name__)

# eBay verification token (32–80 chars, same one you used in eBay form)
VERIFICATION_TOKEN = "ai-ebay-listener-2025-token-for-marketplace-verify"

@app.route('/', methods=['GET', 'POST'])
def ebay_webhook():
    if request.method == 'GET':
        challenge_code = request.args.get('challenge_code')
        if challenge_code:
            return jsonify({'challengeResponse': challenge_code}), 200
        else:
            return "Missing challenge_code", 400

    elif request.method == 'POST':
        data = request.get_json()
        print("Webhook payload received:", data)
        return jsonify({'message': 'Received'}), 200
