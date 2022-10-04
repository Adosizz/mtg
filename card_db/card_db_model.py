from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

#duomnbazes sukurimas
engine = create_engine('sqlite:///MTG_card.db')
Base = declarative_base()

class MTGcard(Base):
    __tablename__ = "Card"
    id = Column(Integer, primary_key=True)
    name = Column("Name", String)
    type = Column("Type", String)
    subtype = Column("Subtype", String)
    mcost = Column("Mana Cost", String)
    cmc = Column("CMC", Integer)
    quant = Column("Quantity", Integer)
    type_id = Column(Integer, ForeignKey("type.id"))
    types = relationship("Type")
    color_id  = Column(Integer, ForeignKey("color.id"))
    colors = relationship("Color")


    def __init__(self, name, type_id, mcost, cmc, quant):
        self.name = name
        self.type_id = type_id
        self.mcost = mcost
        self.quant = quant
        self.cmc = cmc


    def __repr__(self):
        return f"{self.name} {self.type}, {self.mcost},{self.cmc} kiekis {self.quant} "

class Type(Base):
    __tablename__ = 'type'
    id = Column(Integer, primary_key=True)
    type_name = Column('Type', String)
    cards_t = relationship("MTGcard")

    def __init__(self, type_name):
        self.type_name = type_name


    def __repr__(self):
        return f"{self.type_name}"

class Color(Base):
    __tablename__ = "color"
    id = Column(Integer, primary_key=True)
    color_name = Column('Color', String)
    color_c = relationship("MTGcard")


    def __init__(self, color_name):
        self.color_name = color_name


    def __repr__(self):
        return f"{self.color_name}"

class Deck(Base):
    __tablename__ = "Deck"
    id = Column(Integer, primary_key=True)
    name = Column("Name", String)
    format_ = Column("Format", String)
    format_id = Column(Integer, ForeignKey("format.id"))
    formats = relationship("Format")

    def __init__(self, name, format_, format_id ):
        self.name = name
        self.format_ = format_
        self.format_id = format_id

    def __repr__(self):
        return f"{self.name} {self.format_}"

class Format(Base):
    __tablename__ = "format"
    id = Column(Integer, primary_key=True)
    format_ = Column("Format", String)
    deck_f = relationship("Deck")

    def __init__(self, format_):
        self.format_ = format_


    def __repr__(self):
        return f"{self.format_}"






Base.metadata.create_all(engine)