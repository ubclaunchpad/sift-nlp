from flask import Flask
from jobs.registry import run

app = Flask(__name__)

@app.route('/<job>')
def index(job):
    return run(job)

if __name__ == "__main__":
    app.run()
