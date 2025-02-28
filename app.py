from flask import Flask, jsonify, request

app = Flask(__name__)

items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"},
]

@app.route("/", methods=["GET"])
def home():
    return "API is running! Try /api/items"

app.route("/api/items", methods=["GET"])
def get_items():
    return jsonify(items)

app.route("/api/items/<int:id>", methods=["GET"])
def get_item(id):
    item = next((item for item in items if item["id"] == id), None)
    if item:
        return jsonify(item)
    return jsonify({"message": "Item not found"}), 404
if __name__ == "__main__":
    app.run(debug=True)
