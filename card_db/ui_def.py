from card_db.definitions import type_check, checkcolor
from sqlalchemy.orm import sessionmaker
from card_db.models.card_db_model import engine, MtgCard, Deck, session



def add_to_collection(arg, arg2, arg3, arg4, arg5, arg6):
    params = MtgCard(name=arg,
                     type_id=arg2,
                     subtype=arg3,
                     mana_cost=arg4,
                     color_id=arg5,
                     quantity=arg6
                     )
    session.add(params)
    session.commit()



'''
def search_card_image(arg, lbl):
    cards = Card.where(name=arg).all()
    card_variation = []
    for x in (element for element in cards if element.image_url is not None):
        card_variation.append(x.multiverse_id)
    y = Card.find(f"{card_variation[0]}")
    requests.get(f'{y.image_url}', "image.PNG")
    card_image = ImageTk.PhotoImage(Image.open("image.PNG"))
    card_image_label = Label(lbl, image=card_image)
    card_image_label.image = card_image
    card_image_label.grid(row=3, column=2)


def auto_fill(arg, arg2):
    cards = Card.where(name=arg).all()
    card_variation = []
    for x in cards:
        card_variation.append(x.multiverse_id)
    y = Card.find(f"{card_variation[0]}")
    z = type_check(y.type)
    color = checkcolor(y.colors)
    conn = sqlite3.connect('models/MTG_card.db')
    c = conn.cursor()'''
#    with conn:
#        c.execute(f'''INSERT INTO MtgCard(name, type_id, subtype, mana_cost, converted_mana_cost, color_id, quantity)
#               VALUES({y.name}, {z}, {y.subtypes}, {y.mana_cost}, {y.cmc}, {color}, {arg2})''')
#    os.remove("image.PNG")
