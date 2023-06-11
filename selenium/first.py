
from flask import Flask, render_template
from models.deal import Deal
from scraping import scrape_deals
from deals_to_datase import db_sends
from config import app, db
app.template_folder = 'templates'


# Route for triggering the scraping process
@app.route("/scrape")
def run_scraping():
    db_sends()
    return "Scraping completed successfully!"

# Home route
@app.route('/')
def home():
    return "<h1>Welcome to My Deals Aggregator!</h1>"


@app.route('/view')
def ff():
    deals = Deal.query.all()
    return render_template("view.html",data=deals)
if __name__ == '__main__':
    app.run(port=8080)  # Replace 8080 with any available port number
