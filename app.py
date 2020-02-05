from flask import Flask
import json

app = Flask(__name__)


@app.route('/')
def geef_fout():
    return 404 #geeft een foutmelding als de standaard route wordt gekozen


@app.route('/bereken_fouten')
def bereken_fouten():
    return 'kiekeboe'


if __name__ == '__main__':
    app.run()