from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route("/", methods=["GET"])
def home():
    return "API is running! Try /api/items"
if __name__ == "__main__":
    app.run(debug=True)
