from flask import Flask, send_from_directory
from pathlib import Path

app = Flask(__name__)

# Locate the frontend folder beside this file
BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR / "frontend"


@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)