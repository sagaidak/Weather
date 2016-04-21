import urllib
from bs4 import BeautifulSoup

BASE_URL = 'https://pogoda.yandex.ru/'


def get_html(url):
    response = urllib.urlopen(url)
    return response.read()


def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div', {'class': 'current-weather__thermometer current-weather__thermometer_type_now'})

    return div.text


def main():
    city = raw_input('Enter city: ')
    url = BASE_URL + city
    print url
    get_html(url)
    weather = parse(get_html(url))
    print weather


if __name__ == '__main__':
    main()
