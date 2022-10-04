from sqlalchemy.orm import sessionmaker
from card_db_model import engine, Type, Color, Format

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

#Formatu pridejimas

format1 = Format("Standart")
format2 = Format("Modern")
format3 = Format("Historic")
format4 = Format("Legacy")
format5 = Format("Vintage")
format6 = Format("Commander")

session.add(format1)
session.add(format2)
session.add(format3)
session.add(format4)
session.add(format5)
session.add(format6)

session.commit()





