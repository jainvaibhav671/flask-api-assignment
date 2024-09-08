from flask import Flask
from flask_cors import CORS
from .v1.app import v1

app = Flask(__name__)

CORS(app)

app.register_blueprint(v1, url_prefix='/api/v1')

@app.get("/")
def index():
    return "This is a test route"

def dev():
    app.run()

def prod():
    from waitress import serve
    serve(app, host='0.0.0.0', port=5000)

if __name__ == "__main__":
    prod()
