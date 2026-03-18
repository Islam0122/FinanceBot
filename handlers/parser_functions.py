import requests
from bs4 import BeautifulSoup as BS

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
}

def get_detail(movies_name):
    html = requests.get(movies_name, headers=HEADERS)
    soup = BS(html.text, 'html.parser')
    items = soup.find_all('div', class_='entity-desc-description')
    print(items)
    return items

def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('li', class_='results-item-wrap',limit=1)
    # print(items)
    movies = []
    for item in items:
        movies.append({

            "url": f"https://w140.zona.plus{item.find('a').get('href')}",
        })
    print(get_detail(movies[0]["url"]))
    return movies

def get_movies():
    url = "https://w140.zona.plus/movies/avatar-plamya-i-pepel"
    html = requests.get(url, headers=HEADERS)
    data = get_data(html.text)
    return data

def search_movies(name):
    url = "https://w140.zona.plus/search/" + name
    html = requests.get(url, headers=HEADERS)
    data = get_data(html.text)
    return data

get_detail("https://w140.zona.plus/movies/svoi-ballada-o-voine")