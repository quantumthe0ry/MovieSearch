from flask import Flask, request, jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Define search URLs for each site with placeholders for the movie title
SEARCH_URLS = {
    "StreamLord": {"url": "https://streamlord.to/search/{query}", "base": "https://streamlord.to"},
    "123Movies": {"url": "https://w0123movies.com/search/{query}", "base": "https://w0123movies.com"},
    "SolarMovie": {"url": "https://www2.solarmovie.cr/search/{query}/", "base": "https://www2.solarmovie.cr"},
    "123MoviesMe": {"url": "https://www1.123moviesme.online/?s={query}", "base": "https://www1.123moviesme.online"}
}

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
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

    # 123Movies Parsing
    try:
        response = requests.get(SEARCH_URLS["123Movies"]["url"].format(query=query))
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []
        for item in soup.select('.ml-item a.ml-mask'):
            title = item.find('span', class_='mli-info').text.strip()
            link = item['href']
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
        for item in soup.select('.ml-item a.ml-mask'):
            title = item.find('h2').text.strip()
            link = SEARCH_URLS["SolarMovie"]["base"] + item['href']
            results.append({"title": title, "url": link})
        all_results.append({"siteName": SEARCH_URLS["SolarMovie"]["base"], "results": results})
    except Exception as e:
        all_results.append({"siteName": SEARCH_URLS["SolarMovie"]["base"], "results": [], "error": str(e)})

    # 123MoviesMe Parsing
    try:
        response = requests.get(SEARCH_URLS["123MoviesMe"]["url"].format(query=query))
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []
        for item in soup.select('.ml-item a.ml-mask'):
            title = item.find('h2').text.strip()
            link = item['href']
            results.append({"title": title, "url": link})
        all_results.append({"siteName": SEARCH_URLS["123MoviesMe"]["base"], "results": results})
    except Exception as e:
        all_results.append({"siteName": SEARCH_URLS["123MoviesMe"]["base"], "results": [], "error": str(e)})

    # Return all results as JSON
    print(all_results)  # Log results for debugging purposes
    return jsonify(all_results)

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
