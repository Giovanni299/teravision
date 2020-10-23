from flask import Flask, request, jsonify, abort
from src.nested import get_values
from http import HTTPStatus

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>TERAVISION - Challenge </h1>'\
    '<p>Create a web service using any framework that flattens a nested sequence into a single list of values.'

@app.route('/nested', methods=['GET'])
def nested():
    try:
        items = request.get_json()
        data = items['items']
        if type(data) != list:
            return jsonify({'Error':'Value must be a List'}), HTTPStatus.BAD_REQUEST 

        if len(data) < 1:
            return jsonify({'Error':'List empty'}), HTTPStatus.BAD_REQUEST

        return get_values(data)        
    except KeyError:
        return jsonify({'Error':'Parameters erroneous'}), HTTPStatus.BAD_REQUEST

if __name__ == '__main__':
    app.run(debug=False)