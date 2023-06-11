from config import db
from models.deal import Deal
from scrape.i_want_it_all import driver

deals=driver()
deals_arr=[]
def db_sends():
    for i in deals:
        deal = Deal(title=i[0], price=i[-3], discount=i[-1])
        deals_arr.append(deal)
    with db.session.begin_nested():
        for deal in deals_arr:
            db.session.add(deal)
    db.session.commit()