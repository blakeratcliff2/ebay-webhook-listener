import os
import hashlib
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load from environment variable set in Railway
VERIFICATION_TOKEN = os.environ.get("VERIFICATION_TOKEN")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        challenge_code = request.args.get("challenge_code")

        if not challenge_code:
            return "Missing challenge_code", 400
        if not VERIFICATION_TOKEN:
            return "Missing VERIFICATION_TOKEN in environment", 500

        endpoint = request.url_root.rstrip("/")

        # Logging for debugging
        print("----- Incoming GET Request -----")
        print(f"challenge_code: {challenge_code}")
        print(f"endpoint: {endpoint}")
        print(f"VERIFICATION_TOKEN: {VERIFICATION_TOKEN}")

        # Create hash of challengeCode + verificationToken + endpoint
        combined = challenge_code + VERIFICATION_TOKEN + endpoint
        response_hash = hashlib.sha256(combined.encode("utf-8")).hexdigest()

        return jsonify({"challengeResponse": response_hash}), 200

    # Handle POST notifications later
    if request.method == "POST":
        return "", 200

    return "Unsupported method", 405

if __name__ == "__main__":
    app.run(debug=True)


