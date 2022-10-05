from sqlalchemy.orm import sessionmaker
from models.card_db_model import engine, Type, Color

Session = sessionmaker(bind=engine)
session = Session()


# tipų pridėjimas
type1 = Type("Land")
type2 = Type("Artifact")
type3 = Type("Creature")
type4 = Type("Enchantment")
type5 = Type("Instant")
type6 = Type("Planeswalker")
type7 = Type("Sorcery")

session.add(type1)
session.add(type2)
session.add(type3)
session.add(type4)
session.add(type5)
session.add(type6)
session.add(type7)

session.commit()

#Splavų pridėjimas

color1 = Color("Black")
color2 = Color("White")
color3 = Color("Blue")
color4 = Color("Red")
color5 = Color("Green")
color6 = Color("Colorless")

session.add(color1)
session.add(color2)
session.add(color3)
session.add(color4)
session.add(color5)
session.add(color6)

session.commit()






