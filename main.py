from flask import Flask, jsonify, request
from jobs import registry

app = Flask(__name__)

@app.route('/<job>', methods=['POST'])
def index(job):
    if job in registry:
        return jsonify(registry[job](request.get_json()))

if __name__ == "__main__":
    app.run()
