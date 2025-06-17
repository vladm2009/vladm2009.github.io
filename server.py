from flask import Flask, request, send_from_directory, jsonify
import requests, re

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/search')
def search():
    q = request.args.get('q', '')
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f"https://www.youtube.com/results?search_query={q}"
    r = requests.get(url, headers=headers)
    video_ids = list(set(re.findall(r'watch\?v=(\S{11})', r.text)))
    return jsonify(video_ids[:6])

if __name__ == '__main__':
    app.run(port=8080)
