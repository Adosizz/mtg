from tkinter import *
from tkinter import ttk
from ui_def import *
from PIL import Image, ImageTk

def open_deck():
    deck_inside_window = Toplevel()
    deck_inside_window.resizable(False, False)
    deck_inside_box = ttk.Treeview(deck_inside_window, columns=("Nb", "Name", "Type", "Mana Cost", "Quantity"),
                                  show='headings', selectmode='browse')
    for nr, col_heading in enumerate(["Nb", "Name", "Type", "Mana Cost", "Quantity"], 1):
        deck_inside_box.column(f"# {nr}", anchor=W)
        deck_inside_box.heading(f"# {nr}", text=col_heading, anchor=W)
    deck_inside_box.grid(row=1, columnspan=3)
    selected = deck_inside_box.focus()
    values = deck_inside_box.item(selected, 'values')
    conn = sqlite3.connect('models/MTG_card.db')
    c = conn.cursor()
    with conn:
        c.execute(f"SELECT * FROM MtgCard WHERE Deck.id={}")
        records = c.fetchall()

