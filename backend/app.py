from flask import Flask, request, jsonify
from flask_cors import CORS
import json

from intents import parse_input

app = Flask(__name__)
CORS(app)

@app.route("/process", methods=["POST"])
def process():
    data = request.json
    text = data.get("text", "")

    result = parse_input(text)

    with open("storage.json", "a") as f:
        f.write(json.dumps(result) + "\n")

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)