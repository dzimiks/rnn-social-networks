# Search for the best similar matching
# video and opens it in browser

import webbrowser
import requests
from bs4 import BeautifulSoup

query = input("Enter the song to be played: ")
query = query.replace(" ", "+")

# Search for the best similar matching video
url = 'https://www.youtube.com/results?search_query=' + query
source_code = requests.get(url, timeout=15)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, "html.parser")

# Fetches the url of the video
songs = soup.findAll("div", {"class": "yt-lockup-video"})
song = songs[0].contents[0].contents[0].contents[0]
link = song["href"]
webbrowser.open('https://www.youtube.com' + link)