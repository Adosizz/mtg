from tkinter import ttk, Frame, Toplevel, Label, Entry, Button, Tk, W, VERTICAL, DISABLED, StringVar, NO
from models.card_db_model import session, MtgCard, Type, Color, Deck
from PIL import Image, ImageTk
from ui_def import add_to_collection



root = Tk()

root.title("Personal MTG database")
root.geometry("1000x750")
root.resizable(False, False)



#frames

top_frame = Frame(root).grid(row=1)
bottom_frame = Frame(root).grid(row=3)
collection_tree_frame = Frame(root).grid(row=2)
deck_tree_frame = Frame(root).grid(row=4)



#secondary windows
def open_add_card():

    add_card_window = Toplevel()
    add_card_window.resizable(False, False)
    add_card_window.title("Add card to your collection")
    add_label = Label(add_card_window, text="Add card to your collection")
    name_var = StringVar()
    type_var = StringVar()
    subtype_var = StringVar()
    manacost_var = StringVar()
    color_var = StringVar()
    quantity_var = StringVar()
    add_name_label = Label(add_card_window, text="Name")
    add_type_label = Label(add_card_window, text="Type")
    add_subtype_label = Label(add_card_window, text="Subtype")
    add_manacost_label = Label(add_card_window, text="Mana cost")
    add_color_label = Label(add_card_window, text="Color")
    add_quantity_label = Label(add_card_window, text="Quantity")
    add_name_entry = Entry(add_card_window, textvariable=name_var, width=30)
    add_type_entry = Entry(add_card_window, textvariable=type_var, width=30)
    add_subtype_entry = Entry(add_card_window, textvariable=subtype_var, width=30)
    add_manacost_entry = Entry(add_card_window,textvariable=manacost_var, width=30)
    add_color_entry = Entry(add_card_window, textvariable=color_var, width=30)
    add_quantity_entry = Entry(add_card_window,textvariable=quantity_var, width=30)
    add_label.grid(sticky=W)
    add_name_label.grid(row=2, column=0, sticky=W)
    add_type_label.grid(row=3, column=0, sticky=W)
    add_subtype_label.grid(row=4, column=0, sticky=W)
    add_manacost_label.grid(row=5, column=0, sticky=W)
    add_color_label.grid(row=6, column=0, sticky=W)
    add_quantity_label.grid(row=7, column=0, sticky=W)
    add_name_entry.grid(row=2, column=1, sticky=W)
    add_type_entry.grid(row=3, column=1, sticky=W)
    add_subtype_entry.grid(row=4, column=1, sticky=W)
    add_manacost_entry.grid(row=5, column=1, sticky=W)
    add_color_entry.grid(row=6, column=1, sticky=W)
    add_quantity_entry.grid(row=7, column=1, sticky=W)
    search_button = Button(add_card_window, text="search",command=lambda: search_card_image(get_name, add_card_window), state=DISABLED)
    auto_fill_button = Button(add_card_window, text="Auto fill", command=lambda: auto_fill(get_name, get_quantity), state=DISABLED)
    add_to_collection_button = Button(add_card_window, text="Add to collection", command=lambda: add_to_collection(name_var.get(),
                                                                                                                   type_var.get(),
                                                                                                                   subtype_var.get(),
                                                                                                                   manacost_var.get(),
                                                                                                                   color_var.get(),
                                                                                                                   quantity_var.get()))
    add_to_collection_button.grid(row=8, columnspan=2)
    auto_fill_button.grid(row=9, columnspan=2)
    search_button.grid(row=2, column=2)
    back_image = ImageTk.PhotoImage(Image.open("images/cardback.png"))
    card_back_label = Label(add_card_window, image=back_image)
    card_back_label.image = back_image
    card_back_label.grid(rowspan=7, column=2)



def open_deck(event):
    deck_inside_window = Toplevel()
    deck_inside_window.resizable(False, False)
    deck_inside_window.title("Deck")
    deck_inside_box = ttk.Treeview(deck_inside_window, columns=("Nb", "Name", "Type", "Mana Cost", "Quantity"),
                                  show='headings', selectmode='browse')
    for nr, col_heading in enumerate(["Nb", "Name", "Type", "Mana Cost", "Quantity"], 1):
        deck_inside_box.column(f"# {nr}", anchor=W)
        deck_inside_box.heading(f"# {nr}", text=col_heading, anchor=W)
    deck_inside_box.grid(row=1, columnspan=3)
    for x in session.query(MtgCard, Type, Color).join(Type).join(Color).all():
        i = i + 1
        deck_inside_box.insert("", 'end', values=(i, x.name, x.type, x.mana_cost, x.color, x.quantity))




#main window


##Treeviews

collection_box = ttk.Treeview(collection_tree_frame, columns=("id", "Name", "Type", "Mana Cost","Color", "Quantity"),
                              show='headings', selectmode='browse')
for nr, col_heading in enumerate(["id","Name", "Type", "Mana Cost","Color", "Quantity"], 1):
    collection_box.column(f"# {nr}", anchor=W)
    collection_box.heading(f"# {nr}", text=col_heading, anchor=W)
collection_box.column("id", minwidth=0, width=40, stretch=NO)

collection_box.grid(row=4, columnspan=3)
collection_box.bind("<Double-1>", )

deck_box = ttk.Treeview(deck_tree_frame, columns=("id", "name", "format", "description", "Date_created"),
                              show='headings', selectmode='browse')
for nr, col_heading in enumerate(["id","name", "format", "description", "Date_created"], 1):
    deck_box.column(f"# {nr}", anchor=W)
    deck_box.heading(f"# {nr}", text=col_heading, anchor=W)
deck_box.grid(row=8, columnspan=3, sticky=W)
deck_box.bind("<Double-1>", open_deck)


#filling trees

def showcards():
    for x in session.query(MtgCard, Type, Color).join(Type).join(Color).all():
        i = i + 1
        collection_box.insert("", 'end', values=(i, x.name, x.type, x.mana_cost, x.color, x.quantity))
    session.commit()


def showdecks():
    for x in session.query(Deck).all():
        i = i + 1
        deck_box.insert("", 'end', values=(i, x.name, x.type, x.mana_cost, x.color, x.quantity))






##Labels, Buttons, search bars

card_label = Label(top_frame, text="your collection", font=('Times 14')).grid(row=1, column=0)
deck_label = Label(bottom_frame, text="Your decks", font=('Times 14')).grid(row=5, column=0)

add_card_button = Button(top_frame, text="Add card", command=lambda: open_add_card())
delete_card_button = Button(top_frame, text="Delete card")
new_deck_button = Button(bottom_frame, text="New deck")
add_to_deck_button = Button(bottom_frame, text="Add to the deck")
delete_deck_button = Button(bottom_frame, text="Delete deck")

search_label = Label(top_frame, text="Search your collection")
collection_search = Entry(top_frame, width=50)
search_label1 = Label(bottom_frame, text="Search your decks")
deck_search = Entry(top_frame, width=50)

add_card_button.grid(row=2,column=0)
delete_card_button.grid(row=2,column=1)
new_deck_button.grid(row=6, column=0)
add_to_deck_button.grid(row=6, column=1)
delete_deck_button.grid(row=6, column=2)
search_label.grid(row=3,column=0)
search_label1.grid(row=7,column=0)
collection_search.grid(row=3,column=1)
deck_search.grid(row=7,column=1)



#showcards()
showdecks()
root.mainloop()




