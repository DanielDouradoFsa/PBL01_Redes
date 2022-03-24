from flask import Flask, request
from flask_cors import CORS
from flask.json import jsonify
from lixeira import Lixeira
app = Flask("API_Servidor")
CORS(app)

lixeira = Lixeira(500)
lixeira.connect()

@app.route("/putTrash", methods=["POST"])
def putTrash():
    quantity = request.json.get("quantity")
    lixeira.fill(int(quantity))
    return jsonify(lixeira.message), 200

@app.route("/lock", methods=["POST"])
def lock():
    lixeira.lock()
    return jsonify(lixeira.message), 200

@app.route("/unlock", methods=["POST"])
def unlock():
    lixeira.unlock()
    return jsonify(lixeira.message), 200

@app.route("/clear", methods=["POST"])
def clear():
    lixeira.clear()
    return jsonify(lixeira.message), 200    

app.run(host='0.0.0.0', port=3115)
