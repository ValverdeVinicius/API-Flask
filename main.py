from flask import Flask, make_response, jsonify
from bd import paises

app = Flask(__name__)

@app.route('/paises',methods=['GET'])
def get_paises():
    return make_response(jsonify(paises))

app.run()