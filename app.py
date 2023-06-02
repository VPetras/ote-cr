#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import sys

from bs4 import BeautifulSoup


def main():

    ###
    # get website content
    ###

    head = []

    prices = {}

    response = requests.get(
        'https://www.ote-cr.cz/cs/kratkodobe-trhy/elektrina/denni-trh')
    print(response.status_code)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'table report_table'})

    # parsing head
    thead = table.find('thead')
    for row in thead.find_all('tr'):
        for col in row.find_all('th'):
            head.append(col.text.strip())

    # parsing prices
    tbody = table.find('tbody')
    for row in tbody.find_all('tr'):
        try:
            hour = row.find('th').text.strip()
        except AttributeError:
            hour = "Celkem"
        prices[hour] = []
        for col in row.find_all('td'):
            prices[hour].append(col.text.strip())

    with open('table.html', 'w') as f:
        f.write(str(table))
    with open('thead.html', 'w') as f:
        f.write(str(thead))

    with open('tbody.html', 'w') as f:
        f.write(str(tbody))

    with open('head.html', 'w') as f:
        f.write(str(head))
    with open('prices.html', 'w') as f:
        f.write(str(prices))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
