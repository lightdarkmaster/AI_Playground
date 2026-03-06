from server.flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # process data here
    return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
