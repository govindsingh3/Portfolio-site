from flask import Flask, render_template
import os

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))

@app.route('/')
def index():
    return render_template('index.html')

def handler(environ, start_response):
    return app.wsgi_app(environ, start_response)
