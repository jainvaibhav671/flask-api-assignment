from flask import Flask
from .v1.app import v1

app = Flask(__name__)

app.register_blueprint(v1, url_prefix='/api/v1')

@app.get("/")
def index():
    return "This is a test route"

def main():
    app.run()


if __name__ == "__main__":
    main()
