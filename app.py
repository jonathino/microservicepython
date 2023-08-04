from flask import Flask
app = Flask(__name__)

@app.route('/here')
def getWeatherOnline():
    return 'Hoy es un gran dia y me pasan cosas maravillosas!!'