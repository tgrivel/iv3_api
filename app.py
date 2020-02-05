from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route('/')
def geef_fout():
    return 404  # geeft een foutmelding als de standaard route wordt gekozen


@app.route('/bereken_fouten', methods=['GET', 'POST'])
def bereken_fouten():
    posted_data = json.load(request.files['json_bestand'])
    return jsonify(message='kiekeboe')


if __name__ == '__main__':
    app.run()
