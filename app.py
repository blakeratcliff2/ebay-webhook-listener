import os
from flask import Flask, request, jsonify

app = Flask(__name__)

EXPECTED_TOKEN = "ai-ebay-verify-2025-9fB7KxRzLdVpWm82QaJtG3YuNvX0CeLsThAyRfBz"

@app.route("/", methods=["GET"])
def verify_ebay_webhook():
    challenge_code = request.args.get("challenge_code")
    verification_token = request.args.get("verification_token")

    if not challenge_code or not verification_token:
        return "Missing challenge_code or verification_token", 400

    if verification_token != EXPECTED_TOKEN:
        return "Invalid verification token", 403

    return jsonify({"challengeResponse": challenge_code}), 200

@app.route("/health", methods=["GET"])
def health_check():
    return "Webhook listener is live!", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # fallback to 5000 if PORT not set
    app.run(debug=False, host="0.0.0.0", port=port)

