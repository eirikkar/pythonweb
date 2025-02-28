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

app.route("/api/items", methods=["POST"])
def create_item():
    if not request.json or "name" not in request.json:
        return jsonify({"message": "Name is required"}), 400

    new_id = max([item["id"] for item in items]) + 1 if items else 1
    new_item = {"id": new_id, "name": request.json["name"]}
    items.append(new_item)
    
    return jsonify(new_item), 201

if __name__ == "__main__":
    app.run(debug=True)
