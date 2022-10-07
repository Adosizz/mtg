from sqlalchemy.orm import sessionmaker
from card_db_model import engine, Type, Color



Session = sessionmaker(bind=engine)
session = Session()


# tipų pridėjimas
type1 = Type(type_name="Land")
type2 = Type(type_name="Artifact")
type3 = Type(type_name="Creature")
type4 = Type(type_name="Enchantment")
type5 = Type(type_name="Instant")
type6 = Type(type_name="Planeswalker")
type7 = Type(type_name="Sorcery")

session.add(type1)
session.add(type2)
session.add(type3)
session.add(type4)
session.add(type5)
session.add(type6)
session.add(type7)

session.commit()

#Splavų pridėjimas

color1 = Color(color_name="Black")
color2 = Color(color_name="White")
color3 = Color(color_name="Blue")
color4 = Color(color_name="Red")
color5 = Color(color_name="Green")
color6 = Color(color_name="Colorless")

session.add(color1)
session.add(color2)
session.add(color3)
session.add(color4)
session.add(color5)
session.add(color6)

session.commit()






