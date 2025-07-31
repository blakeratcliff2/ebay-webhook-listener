from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify_ebay():
    challenge_code = request.args.get('challenge_code')
    if challenge_code:
        return jsonify({"challengeResponse": challenge_code}), 200
    return "Missing challenge_code", 400

@app.route('/health', methods=['GET'])
def health_check():
    return "Webhook is running", 200

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
