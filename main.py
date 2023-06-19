# get our stock price and % change
# paste data into csv

# proper class for % is next to jsname="m6NnIb"
# and over div class="JwB6zf V7hZne"


import requests
from bs4 import BeautifulSoup
import csv
import time
from datetime import date
import webbrowser


stock_urls = {
    'Apple': 'https://www.google.com/finance/quote/AMZN:NASDAQ',
    'Amazon': 'https://www.google.com/finance/quote/AAPL:NASDAQ',
    'Invesco': 'https://www.google.com/finance/quote/QQQ:NASDAQ'
}
stock_symbols = {
    'Apple': 'APPL',
    'Amazon': 'AMZN',
    'Invesco': 'QQQ'
}


def get_soup(url):
    while True:
        response = requests.get(url)
        if response.status_code == 200:
            print('Request Succeeded')

            break
        else:
            print(f'Request Failed: {response.status_code}')
            time.sleep(.1)
            continue

    # webpage
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def grab_ind_stock(text, symbol):
    monetary_value = text.find("div", class_="YMlKec fxKbKc").get_text()

    return [symbol, monetary_value]


def grab_data(url, symbol):
    soup = get_soup(url)
    return grab_ind_stock(soup, symbol)


def get_all_data():
    all_data = []
    for key in stock_urls:
        url = stock_urls[key]
        sym = stock_symbols[key]
        all_data.append(grab_data(url, sym))

    return all_data


def add_to_csv(file, list):
    with open(file, 'w', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([
            'Symbol',
            'Value per Share'
        ])
        csv_writer.writerows(list)


if __name__ == '__main__':
    all_data = get_all_data()
    print(all_data)
    add_to_csv(f'stocks_{date.today()}.csv', all_data)

