from server.flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # process data here
    prediction = data.get('input', 'no input provided') if data else 'no data'
    return jsonify({'result': 'success', 'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
