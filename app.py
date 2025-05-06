from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello Dionar, I love you ❤️'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use dynamic port or default to 5000
    app.run(host='0.0.0.0', port=port)
