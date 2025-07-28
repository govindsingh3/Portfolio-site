from flask import Flask, render_template
import os

# Correct folder paths
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
static_dir = os.path.join(os.path.dirname(__file__), 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route('/')
def index():
    return render_template('index.html')

# Required for Vercel Serverless
def handler(event, context):
    from werkzeug.middleware.dispatcher import DispatcherMiddleware
    from werkzeug.wrappers import Response

    def simple_app(environ, start_response):
        res = Response("Not Found", status=404)
        return res(environ, start_response)

    app_dispatch = DispatcherMiddleware(simple_app, {
        "/": app
    })

    return app_dispatch(event, context)

def handler(environ, start_response):
    return app.wsgi_app(environ, start_response)
