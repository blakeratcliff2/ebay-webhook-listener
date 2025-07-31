from flask import Flask, request, jsonify
import hashlib
import os

app = Flask(__name__)

# Load from environment (Railway variable)
VERIFICATION_TOKEN = os.environ.get("VERIFICATION_TOKEN")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        challenge_code = request.args.get("challenge_code")
        endpoint = request.base_url

        print("----- Incoming GET Request -----")
        print("challenge_code:", challenge_code)
        print("endpoint:", endpoint)
        print("VERIFICATION_TOKEN:", VERIFICATION_TOKEN)

        # Validate inputs
        if not challenge_code or not VERIFICATION_TOKEN or not endpoint:
            return "Missing challenge_code or VERIFICATION_TOKEN", 400

        # Concatenate and hash
        concat = challenge_code + VERIFICATION_TOKEN + endpoint
        hash_obj = hashlib.sha256(concat.encode("utf-8"))
        challenge_response = hash_obj.hexdigest()

        return jsonify({"challengeResponse": challenge_response})

    if request.method == "POST":
        print("----- Incoming POST Notification -----")
        print(request.json)
        return "", 200

    return "Unsupported method", 405


