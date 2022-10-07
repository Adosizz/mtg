from mtgsdk import Card
from urllib import request
from PIL import Image
import sqlite3
from card_db.definitions import *

def search_card_image(arg, lbl):
    cards = Card.where(name=arg).all()
    card_variation = []
    for x in (element for element in cards if element.image_url is not None):
        card_variation.append(x.multiverse_id)
    y = Card.find(f"{card_variation[0]}")
    request.urlretrieve(f'{y.image_url}', "image.PNG")
    card_image = ImageTk.PhotoImage(Image.open("image.PNG"))
    card_image_label = Label(lbl, image=card_image)
    card_image_label.image = card_image
    card_image_label.grid(row=3, column=2)

def add_to_collection(arg, arg2):
    cards = Card.where(name=arg).all()
    card_variation = []
    for x in cards:
        card_variation.append(x.multiverse_id)
    y = Card.find(f"{card_variation[0]}")
    z = type_check(y.type)
    conn = sqlite3.connect('models/MTG_card.db')
    c = conn.cursor()
    with conn:
        c.execute(f'''INSERT INTO MtgCard(name, type_id, subtype, mana_cost, converted_mana_cost, color_id, quantity)
               VALUES({y.name}, {z}, {y.subtypes}, {y.manaCost}, {y.cmc}, {y.colors}, {arg2})
     ''')
    os.remove("image.PNG")


def select_item_deck():
    selected = deck_box.focus()
    values = deck_box.item(selected, 'values')
    return values


#def query_database():
#   conn = sqlite3.connect('models/MTG_card.db')
#    c = conn.cursor()
#    c.execute("SELECT * FROM Deck")
#    records = c.fetchall()
#    count = 0
#    for record in records:
#        deck_box.insert('', tk.END, values=record)
#        count += 1
#    conn.commit()
#    conn.close()