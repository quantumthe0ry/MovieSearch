# MovieSearch

I have a few websites bookmarked on my Firestick that I occasionally use to watch movies and series. It’s tedious to visit each site individually to search for a specific title, so I created this simple website to search all of them at once. This is a personal project to automate the process and save time. I’m not a developer—just someone who got bored and decided to make life a little easier!

- **Update** - My dog ate my firestick remote making it difficult to type text, so I wanted a way to search for movies/series without a remote. I added some routes to app.py, added a polling functionality to webpage.html, and created remote.html. Now when the app is running, you can use remote.html from a computer or mobile device to send queries to webpage.html instead of having to type them manually.

## What's Included

- **webpage.html** - A straightforward HTML page with a search input. When you enter a movie or series title and hit search, it sends the query to the backend, which then queries the specified websites and displays the results. The results from each site are organized and separated by dividers for easy viewing. In addition to manual input, the page also checks for remote search queries sent from other devices (like a phone or computer) once per minute. If a remote query is found, it is automatically populated into the search field and executed — allowing full remote control without using the TV remote.

- **remote.html** - A lightweight HTML page designed for sending movie or series search queries to the TV remotely. It provides a simple input field and a "Send" button. When submitted, the query is sent to the backend, which stores it for one-time use. The webpage.html running on the TV polls for these remote queries and automatically executes them, allowing you to initiate searches from any device on the network without needing to type using the TV remote.

- **app.py** - The backend code that powers the search functionality. It uses Flask to create an API endpoint, which receives the search query from webpage.html. This script is configured to search specific movie streaming websites for the given query, parse the HTML responses, and extract the URLs of the search results. It then sends these results back to webpage.html to display.
Additionally, it includes support for remote search control via remote.html, allowing other devices to submit queries that are automatically picked up and executed by webpage.html.

- **favicon.ico** - A simple favicon to make the website look a little more polished in the browser. It’s not necessary but adds a nice touch.
- **logo.png** - it is what it is

## How It Works

1. **Start the Backend Server**  
   Run `app.py` using Python to start the Flask server. This server handles all incoming search requests and manages query distribution between interfaces.

2. **Serve the Web Interface**  
   Use a browser (like TV Bro on a Firestick or any browser on your computer) to open `webpage.html`. You can serve this file locally using a simple HTTP server such as Python’s `http.server`.

3. **Search via TV or Remotely**  
   - **On the TV**: Enter a movie or series title into the search bar on `webpage.html` and click **Search**.  
   - **Remotely**: Open `remote.html` from another device (phone, laptop, etc.), enter a query, and click **Send**. The TV will automatically receive and run the search. It checks for remote queries once per minute.

4. **Backend Processing**  
   The backend (`app.py`) receives the query, searches the specified movie streaming websites, parses the HTML responses, and extracts matching titles and links.

5. **Results Displayed**  
   The backend returns the search results to `webpage.html`, where they are displayed cleanly by site. Each group of results is separated by a visual divider for easy viewing.


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
   git clone https://github.com/quantumthe0ry/MovieSearch.git
   ```
2. Navigate into the project directory:
   ```bash
   cd MovieSearch
   ```
3. Start the backend server:
   ```bash
   python3 app.py
   ```
4. Set the correct IP on Line 78 and 114 in webpage.html, then in a new terminal window, serve webpage.html using a simple HTTP server:
   ```bash
   python3 -m http.server 80
   ```
5. Open a browser and navigate to http://192.168.0.X/webpage.html (Replace the IP with the IP running the server)
6. Optional use: remote.html. Once webpage.html is loaded, you can use remote.html to send remote queries to the webpage. This way you can use your mobile device or computer to type queries instead of a remote. Make sure to edit line 52 to reflect the correct IP address.

# Limitations
Some websites may have CAPTCHA or anti-bot measures that prevent automated querying. One of the sites I use initiates a Cloudflare human check for each search query. I initially tried to use Selenium to bypass this but was ultimately not successful. It may be possible, but again, I'm not a developer, so it's a little over my head. Therefore, I chose to exclude that site.
