#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from config import db
from models.deal import Deal


def scrape_deals():
    url = "https://www.amazon.com"  # Replace with the URL of the specific Amazon page you want to scrape
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    deals = []

    # Locate and extract the deal information using BeautifulSoup
    # For example:
    deal_elements = soup.find_all("div", class_="deal-element")
    for deal_element in deal_elements:
        title = deal_element.find("h3").text.strip()
        price = deal_element.find("span", class_="price").text.strip()
        discount = deal_element.find("span", class_="discount").text.strip()

        deal = models.Deal(title=title, price=price, discount=discount)
        deals.append(deal)

    # Store the scraped deals in the database
    with db.session.begin_nested():
        for deal in deals:
            db.session.add(deal)
    db.session.commit()

