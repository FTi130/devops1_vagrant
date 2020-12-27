from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    return {
        'Date': datetime.utcnow().strftime('%d %B %Y'),
        'User-Agent': request.headers.get('User-Agent')
    }

if __name__ == "__main__":
    app.run()
