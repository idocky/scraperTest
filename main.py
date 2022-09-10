import requests
import bs4
from sqlalchemy.orm import Session
from models import Ads
from db import SessionLocal, engine
import models
from datetime import date
import re

models.Base.metadata.create_all(bind=engine)
session = Session()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def link_generate(page: int) -> str:
    return f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{page}/c37l1700273'

def parse_data(url: str, session: Session):
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    ads = soup.find_all('div', class_='search-item')
    for ad in ads:
        dated_at = ad.find(class_='date-posted').text
        if not dated_at[-1].isnumeric():
            dated_at = date.today()


        try:
            price = float(ad.find(class_='price').text.strip()[1:].replace(',', ''))
        except:
            price = 0
        ad = Ads(
            picture=ad.find('img').get('data-src'),
            title = ad.find(class_='title').text.strip(),
            city = ad.find(class_='location').find('span').text.strip(),
            date = dated_at,
            beds = ad.find(class_='bedrooms').text.strip().split('\n')[1].strip(),
            content = ad.find(class_='description').text.strip().split('...')[0],
            price = price,
            currency = ad.find(class_='price').text.strip()[0],
        )
        session.add(ad)
        session.commit()





for page in range(1, 92):
    parse_data(link_generate(page), SessionLocal)
