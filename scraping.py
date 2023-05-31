import requests
from bs4 import BeautifulSoup
from models.deal import Deal
from config import db

def scrape_deals():
    url = "https://www.amazon.com/gp/goldbox"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    deals = []

    # Locate and extract the deal information using BeautifulSoup
    deal_elements = soup.select(".dealTile")
    for deal_element in deal_elements:
        title_element = deal_element.select_one(".dealTitle")
        price_element = deal_element.select_one(".priceBlock")
        discount_element = deal_element.select_one(".dealPriceText")

        if title_element and price_element and discount_element:
            title = title_element.text.strip()
            price = price_element.text.strip()
            discount = discount_element.text.strip()

            deal = Deal(title=title, price=price, discount=discount)
            deals.append(deal)

    # Store the scraped deals in the database
    with db.session.begin_nested():
        for deal in deals:
            db.session.add(deal)
    db.session.commit()
