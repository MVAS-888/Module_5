from flask import Flask, request, jsonify
from shortener import URLShortener

app = Flask(__name__)
shortener = URLShortener()

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    long_url = data.get("url")
    
    if not long_url:
        return jsonify({"error": "URL не надано"}), 400
    
    short_url = shortener.shorten(long_url)
    return jsonify({"short_url": short_url})

@app.route('/expand/<short_url>', methods=['GET'])
def expand_url(short_url):
    long_url = shortener.expand(short_url)
    
    if long_url == "URL не знайдено":
        return jsonify({"error": "URL не знайдено"}), 404
    
    return jsonify({"long_url": long_url})

if __name__ == "__main__":
    app.run(debug=True)

