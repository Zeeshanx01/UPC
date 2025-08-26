
#? run this command: "uv run python main02.py"

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
app.run()
