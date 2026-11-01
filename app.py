
from flask import Flask, request, jsonify, send_from_directory
from modules.url_analysis import analyze_url

app = Flask(__name__, static_folder="frontend")

@app.route("/")
def home():
    return send_from_directory("frontend", "index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()
    url = data.get("url", "").strip()

    if not url:
        return jsonify({"error": "Please enter a URL"}), 400

    result = analyze_url(url)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
