from flask import Flask, render_template
import requests
from quote import *

app = Flask(__name__,template_folder="template")


@app.route('/')
def index():
    api = 'https://api.ipify.org/'
    ip = requests.get(api).text
    anime = quote_data['anime']
    character= quote_data['character']
    quote = quote_data['quote']

    return render_template('index.html', anime=anime, character=character, quote=quote, ip=ip)
if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)