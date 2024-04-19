#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests as r
url = "https://scpfoundation.net/scp-"
for element in range(400, 1000):
    contents = r.get(url + str(element).rjust(3, "0")).text
    print("downloaded:", element)
    soup = BeautifulSoup(contents, "html.parser")
    rating = soup.find("span", {'class': 'w-stars-rate-number'})
    if rating is None:
        continue
    rating = rating.text
    try:
        rating = float(rating)
    except ValueError:
        print(f"{element}: {rating}")
        continue
    if float(rating) > 4.0:
        print(f"{element}: {rating}")
quit()
