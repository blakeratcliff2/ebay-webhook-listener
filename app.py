import os
import hashlib
from flask import Flask, request, jsonify

app = Flask(__name__)

# Get the verification token from Railway environment variable
VERIFICATION_TOKEN = os.environ.get("VERIFICATION_TOKEN")

# Must match the URL eBay uses to send the challenge (with https and trailing slash)
ENDPOINT = "https://web-production-98b2f.up.railway.app/"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        challenge_code = request.args.get("challenge_code")
        print("----- Incoming GET Request -----")
        print(f"challenge_code: {challenge_code}")
        print(f"endpoint: {ENDPOINT}")
        print(f"VERIFICATION_TOKEN: {VERIFICATION_TOKEN}")

        if not challenge_code or not VERIFICATION_TOKEN:
            return jsonify({"error": "Missing challenge_code or VERIFICATION_TOKEN"}), 400

        # Hash using: challenge_code + VERIFICATION_TOKEN + endpoint
        combined = challenge_code + VERIFICATION_TOKEN + ENDPOINT
        challenge_response = hashlib.sha256(combined.encode('utf-8')).hexdigest()

        return jsonify({"challengeResponse": challenge_response}), 200

    elif request.method == "POST":
        # Handle actual deletion notification here
        data = request.get_json()
        print("----- Incoming POST Notification -----")
        print(data)
        return '', 204  # Respond with 204 to acknowledge

if __name__ == "__main__":
    app.run(debug=True)



