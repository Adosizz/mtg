from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Table

#duomnbazes sukurimas
engine = create_engine('sqlite:///MTG_card.db')
Base = declarative_base()

class MtgCard(Base):
    __tablename__ = "Card"
    id = Column(Integer, primary_key=True)
    name = Column("Name", String)
    subtype = Column("Subtype", String)
    mana_cost = Column("Mana Cost", String)
    converted_mana_cost = Column("CMC", Integer)
    quantity = Column("Quantity", Integer)
    type_id = Column(Integer, ForeignKey("type.id"))
    types = relationship("type")
    color_id  = Column(Integer, ForeignKey("color.id"))
    colors = relationship("color")


    def __init__(self, name, type_id, mana_cost, converted_mana_cost, quantity):
        self.name = name
        self.type_id = type_id
        self.mana_cost = mana_cost
        self.quantity = quantity
        self.converted_mana_cost = converted_mana_cost


    def __repr__(self):
        return f"{self.name} {self.type}, {self.mana_cost},{self.converted_mana_cost} kiekis {self.quantity} "

class Type(Base):
    __tablename__ = 'type'
    id = Column(Integer, primary_key=True)
    type_name = Column('Type', String)


    def __init__(self, type_name):
        self.type_name = type_name


    def __repr__(self):
        return f"{self.type_name}"

class Color(Base):
    __tablename__ = "color"
    id = Column(Integer, primary_key=True)
    color_name = Column('Color', String)



    def __init__(self, color_name):
        self.color_name = color_name


    def __repr__(self):
        return f"{self.color_name}"

link_table = Table(
    "association",
    Base.metadata,
    Column("Deck_id", ForeignKey("Deck.id")),
    Column("Card_id", ForeignKey("Card.id")),
)


class Deck(Base):
    __tablename__ = "Deck"
    id = Column(Integer, primary_key=True)
    name = Column("Name", String)
    format_name = Column("Format", String)
    cards = relationship('Card', secondary=link_table)


    def __init__(self, name, format_name):
        self.name = name
        self.format_name = format_name


    def __repr__(self):
        return f"{self.name} {self.format_name}"




Base.metadata.create_all(engine)