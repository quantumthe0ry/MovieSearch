# MovieSearch

I have a few websites bookmarked on my Firestick that I occasionally use to watch movies and series. It’s tedious to visit each site individually to search for a specific title, so I created this simple website to search all of them at once. This is a personal project to automate the process and save time. I’m not a developer—just someone who got bored and decided to make life a little easier!

## What's Included

- **webpage.html** - A straightforward HTML page with a search input. When you enter a movie or series title and hit search, it sends the query to the backend, which then queries the specified websites and displays the results. The results from each site are organized and separated by dividers for easy viewing.

- **app.py** - The backend code that powers the search functionality. It uses Flask to create an API endpoint, which receives the search query from `webpage.html`. This script is configured to search specific movie streaming websites for the given query, parse the HTML responses, and extract the URLs of the search results. It then sends these results back to `webpage.html` to display.

- **favicon.ico** - A simple favicon to make the website look a little more polished in the browser. It’s not necessary but adds a nice touch.
- **logo.png** - it is what it is

## How It Works

1. **Start the Backend Server**: Run `app.py` using Python to start the Flask server. This server listens for search requests sent from `webpage.html`.
   
2. **Open the Web Interface**: Use a browser (like TV Bro on a Firestick or any browser on your computer) to open `webpage.html`. You can serve this HTML file locally using a simple HTTP server, such as Python’s `http.server`.

3. **Enter a Search Query**: In the search bar, enter the title of the movie or series you’re looking for and hit search. This sends the query to the backend (`app.py`).

4. **Backend Processing**: The backend (`app.py`) takes the query, searches each specified website, and parses the HTML responses to find the search results.

5. **Display Results**: The backend sends the search results back to `webpage.html`, where they are displayed neatly by site, with each site’s results separated by dividers.

## Requirements

- **Python 3.x** with `Flask` and `BeautifulSoup` libraries.
  - You can install Flask and BeautifulSoup with:
    ```bash
    pip install flask beautifulsoup4
    ```
- **A Web Browser**: Any modern browser will work. This was designed for TV Bro on Firestick, but it works just as well on desktop browsers.

## Running the Project

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/MovieSearch.git
   ```
2. Navigate into the project directory:
   ```bash
   cd MovieSearch
   ```
3. Start the backend server:
   ```bash
   python3 app.py
   ```
4. Set the correct IP on Line 49 in webpage.html, then in a new terminal window, serve webpage.html using a simple HTTP server:
   ```bash
   python3 -m http.server 80
   ```
5. Open a browser and navigate to http://192.168.0.X/webpage.html (Replace the IP with the IP running the server)

# Limitations
Some websites may have CAPTCHA or anti-bot measures that prevent automated querying. One of the sites I use initiates a Cloudflare human check for each search query. I initially tried to use Selenium to bypass this but was ultimately not successful. It may be possible, but again, I'm not a developer, so it's a little over my head. Therefore, I chose to exclude that site.
