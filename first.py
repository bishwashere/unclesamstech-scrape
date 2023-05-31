
from flask import Flask
from scraping import scrape_deals

from app_main import app
# Route for triggering the scraping process
@app.route("/scrape")
def run_scraping():
    scrape_deals()
    return "Scraping completed successfully!"

# Home route
@app.route('/')
def home():
    return "<h1>Welcome to My Deals Aggregator!</h1>"

if __name__ == '__main__':
    app.run(port=8080)  # Replace 8080 with any available port number
