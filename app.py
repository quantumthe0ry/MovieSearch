from flask import Flask, request, jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Define search URLs for each site with placeholders for the movie title
SEARCH_URLS = {
    "StreamLord": {"url": "https://streamlord.to/search/{query}", "base": "https://streamlord.to"},
    "123Movies": {"url": "https://moviehdpoint.com/search/{query}", "base": "https://moviehdpoint.com"},
    "SolarMovie": {"url": "https://solarmovie.vip/movie/search/{query}/", "base": "https://solarmovie.vip"},
    "bMovies": {"url": "https://ww.bmovies.vip/movie/search/{query}", "base": "https://bmovies.vip"},
    "Putlocker": {"url": "https://ww4.putlocker.vip/movie/search/{query}", "base": "https://ww4.putlocker.vip"}
}

# Global store for one-time remote query
pending_query = {"value": None}

@app.route('/remote-query', methods=['POST'])
def set_remote_query():
    data = request.get_json()
    query = data.get('query', '').strip()
    if query:
        pending_query["value"] = query
        return jsonify({"status": "OK", "message": f"Query set to: {query}"})
    return jsonify({"status": "error", "message": "No query provided"}), 400

@app.route('/get-remote-query', methods=['GET'])
def get_remote_query():
    query = pending_query["value"]
    pending_query["value"] = None  # one-time use
    return jsonify({"query": query})

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').replace(' ', '+')
    if not query:
        return jsonify({"error": "No query provided"}), 400

    all_results = []

    # StreamLord Parsing
    try:
        response = requests.get(SEARCH_URLS["StreamLord"]["url"].format(query=query))
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []
        for item in soup.select('.ml-item a.ml-mask'):
            title = item['title']
            link = SEARCH_URLS["StreamLord"]["base"] + item['href']
            results.append({"title": title, "url": link})
        all_results.append({"siteName": SEARCH_URLS["StreamLord"]["base"], "results": results})
    except Exception as e:
        all_results.append({"siteName": SEARCH_URLS["StreamLord"]["base"], "results": [], "error": str(e)})

    # 123Movies (moviehdpoint.com) Parsing
    try:
        response = requests.get(SEARCH_URLS["123Movies"]["url"].format(query=query), timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []
        for item in soup.select('.ml-item'):
            a_tag = item.select_one('a.ml-mask')
            h2_tag = item.select_one('h2')
            if a_tag and h2_tag:
                title = h2_tag.text.strip()
                link = a_tag['href'].strip()
                results.append({"title": title, "url": link})
        all_results.append({"siteName": SEARCH_URLS["123Movies"]["base"], "results": results})
    except Exception as e:
        all_results.append({"siteName": SEARCH_URLS["123Movies"]["base"], "results": [], "error": str(e)})

    # SolarMovie Parsing
    try:
        response = requests.get(SEARCH_URLS["SolarMovie"]["url"].format(query=query))
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []
        for item in soup.select('.ml-item .ml-mask'):
            title = item['title'].strip()
            link = SEARCH_URLS["SolarMovie"]["base"] + item['href']
            results.append({"title": title, "url": link})
        all_results.append({"siteName": SEARCH_URLS["SolarMovie"]["base"], "results": results})
    except Exception as e:
        all_results.append({"siteName": SEARCH_URLS["SolarMovie"]["base"], "results": [], "error": str(e)})

    # bMovies Parsing
    try:
        response = requests.get(SEARCH_URLS["bMovies"]["url"].format(query=query))
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []
        for item in soup.select('.ml-item .ml-mask'):
            title = item['title'].strip()
            link = SEARCH_URLS["bMovies"]["base"] + item['href']
            results.append({"title": title, "url": link})
        all_results.append({"siteName": SEARCH_URLS["bMovies"]["base"], "results": results})
    except Exception as e:
        all_results.append({"siteName": SEARCH_URLS["bMovies"]["base"], "results": [], "error": str(e)})

    # Putlocker Parsing
    try:
        response = requests.get(SEARCH_URLS["Putlocker"]["url"].format(query=query))
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []
        for item in soup.select('.ml-item .ml-mask'):
            title = item['title'].strip()
            link = SEARCH_URLS["Putlocker"]["base"] + item['href']
            results.append({"title": title, "url": link})
        all_results.append({"siteName": SEARCH_URLS["Putlocker"]["base"], "results": results})
    except Exception as e:
        all_results.append({"siteName": SEARCH_URLS["Putlocker"]["base"], "results": [], "error": str(e)})

    print(all_results)  # For debugging
    return jsonify(all_results)

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
