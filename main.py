from flask import Flask, render_template, send_file
from pathlib import Path
from PIL import Image

app = Flask(__name__)

def find_ims():
    base_dir = Path("images")
    ims = list(base_dir.glob("*.jpg"))
    return ims

@app.route("/images/<name>")
def serve_im(name):
    return send_file(f"images/{name}")

@app.route("/")
def hello_world():
    output = [str(x) for x in find_ims()]
    return render_template("list.html", output=output)