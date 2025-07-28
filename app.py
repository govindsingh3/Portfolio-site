from flask import Flask, render_template
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
static_dir = os.path.join(os.path.dirname(__file__), 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route('/')
def index():
    return render_template('index.html')

# Required by Vercel
def handler(environ, start_response):
    return app.wsgi_app(environ, start_response)
