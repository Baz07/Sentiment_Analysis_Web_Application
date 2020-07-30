from flask import Flask, send_file, make_response, session
from flask import request, jsonify
import matplotlib.pyplot as plt
import io
from M0_main import code
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.config['DEBUG'] = True
cors = CORS(app)

## Homepage Route
@app.route('/', methods = ['GET'])
def home():
    return "<h1> Welcome </h1>"

## Form Connection and Data Delivery API Route
@app.route('/word', methods = ['GET', 'POST'])
def wordspace():
    if request.method == 'GET':
        place = request.args.get('place')
        data = code(place)
        data = data[0]
        return jsonify(data)

app.run()
