from flask import Flask, request

app = Flask(__name__)


@app.route('/status/', methods=["GET", "POST"])
def custom_status_code():
    if request.method == "GET":
        return "Response GET method"
    return "Response POST method"