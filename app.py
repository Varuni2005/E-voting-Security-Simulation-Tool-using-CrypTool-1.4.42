from flask import Flask, render_template, request, jsonify
from security.aes_module import AESModule
from security.hash_module import HashModule
from security.rsa_module import RSAModule
from security.tls_module import TLSModule

app = Flask(__name__)

aes = AESModule()
rsa = RSAModule()

@app.route("/")
def home():
    return render_template("index.html")


# AES Encrypt
@app.route("/encrypt", methods=["POST"])
def encrypt():
    text = request.json["text"]
    encrypted = aes.encrypt(text)
    return jsonify({"result": encrypted})


# AES Decrypt
@app.route("/decrypt", methods=["POST"])
def decrypt():
    try:
        text = request.json["text"]
        decrypted = aes.decrypt(text)
        return jsonify({"result": decrypted})
    except Exception:
        return jsonify({"result": "Decryption Failed"}), 400


# SHA-256 Hash
@app.route("/hash", methods=["POST"])
def hash_data():
    text = request.json["text"]
    hashed = HashModule.sha256_hash(text)
    return jsonify({"result": hashed})


# RSA Sign
@app.route("/sign", methods=["POST"])
def sign():
    text = request.json["text"]
    signature = rsa.sign(text)
    return jsonify({"result": signature})


# RSA Verify
@app.route("/verify", methods=["POST"])
def verify():
    text = request.json["text"]
    signature = request.json["signature"]
    valid = rsa.verify(text, signature)
    return jsonify({"result": valid})


# TLS Check
@app.route("/tls", methods=["GET"])
def tls():
    return jsonify(TLSModule.test_tls_connection())


if __name__ == "__main__":
    app.run(debug=True)
