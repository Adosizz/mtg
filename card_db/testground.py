from mtgsdk import Card
from sqlalchemy.orm import sessionmaker
from card_db_model import engine, MTGcard





 #   for elem in card.image_url:

Session = sessionmaker(bind=engine)
session = Session()

tevas = session.query(MTGcard).get(1)
print(Card.name)



