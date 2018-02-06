# Script googles the keyword and opens
# top 5 (max) search results in separate
# tabs in the browser

import webbrowser
import requests
import bs4

def search_keyword():
    keyword = input("Insert keyword: ")
    res = requests.get('http://google.com/search?q=' + keyword)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html5lib")
    link_elements = soup.select('.r a')
    num_open = min(5, len(link_elements))

    for i in range(num_open):
        webbrowser.open('http://google.com' + link_elements[i].get('href'))

if __name__ == '__main__':
    search_keyword()