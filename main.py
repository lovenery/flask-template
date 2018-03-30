from flask import Flask, render_template, jsonify, request
from os import environ
from helper.flask_cors import add_cors_headers

app = Flask(__name__)
app.after_request(add_cors_headers)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port = int(environ.get("PORT", 5000)))
