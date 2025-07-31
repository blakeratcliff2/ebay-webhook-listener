# app.py
from flask import Flask, request, jsonify
import hashlib
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

VERIFICATION_TOKEN = os.getenv("EBAY_VERIFICATION_TOKEN")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        challenge_code = request.args.get("challenge_code")
        endpoint = request.base_url

        if not challenge_code:
            return "Missing challenge_code", 400

        concat = challenge_code + VERIFICATION_TOKEN + endpoint
        response_hash = hashlib.sha256(concat.encode("utf-8")).hexdigest()

        print(f"Returning challengeResponse: {response_hash}")
        return jsonify({"challengeResponse": response_hash})

    elif request.method == "POST":
        print("Received POST (notification):")
        print(request.get_json())
        return '', 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

