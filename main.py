from flask import Flask, request, jsonify
from function.decode2Share import decode2Share

from function.encodeFromBase64 import encodeFromBase64

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.post("/encode")
def endcode():
    formData = (request.form).to_dict()
    print(formData)
    print(formData['imageBase64'])
    imageBase64 = formData["imageBase64"]
    result = encodeFromBase64(imageBase64)
    print(result)
    return jsonify(result)

@app.post("/decode")
def decode():
    formData = (request.form).to_dict()
    
    share1 = formData['share1']
    share2 = formData['share2']
    result = decode2Share(share1 , share2)
    return result