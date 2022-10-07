from tkinter import ttk, Frame, Toplevel, Label, Entry, Button, Tk, W
from ui_def import search_card_image, add_to_collection, query_database
from PIL import Image, ImageTk



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
    add_name_label = Label(add_card_window, text="Name")
    add_type_label = Label(add_card_window, text="Type")
    add_subtype_label = Label(add_card_window, text="Subtype")
    add_manacost_label = Label(add_card_window, text="Mana cost")
    add_color_label = Label(add_card_window, text="Color")
    add_quantity_label = Label(add_card_window, text="Quantity")
    add_name_entry = Entry(add_card_window, width=30)
    add_type_entry = Entry(add_card_window, width=30)
    add_subtype_entry = Entry(add_card_window, width=30)
    add_manacost_entry = Entry(add_card_window, width=30)
    add_color_entry = Entry(add_card_window, width=30)
    add_quantity_entry = Entry(add_card_window, width=30)
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
    get_name = add_name_entry.get()
    get_quantity = add_quantity_entry.get()
    search_button = Button(add_card_window, text="search", command=lambda: search_card_image(get_name, add_card_window))
    add_to_collection_button = Button(add_card_window, text="Add to collection", command=lambda: add_to_collection(get_name, get_quantity))
    add_to_collection_button.grid(row=8, columnspan=2)
    search_button.grid(row=2, column=2)
    back_image = ImageTk.PhotoImage(Image.open("images/cardback.png"))
    card_back_label = Label(add_card_window, image=back_image)
    card_back_label.image = back_image
    card_back_label.grid(rowspan=7, column=2)

#def open_deck():







#main window




##Treeviews

collection_box = ttk.Treeview(collection_tree_frame, columns=("Nb","Name", "Type", "Mana Cost", "Quantity"),
                              show='headings', selectmode='browse')
for nr, col_heading in enumerate(["Nb","Name", "Type", "Mana Cost", "Quantity"], 1):
    collection_box.column(f"# {nr}", anchor=W)
    collection_box.heading(f"# {nr}", text=col_heading, anchor=W)
collection_box.grid(row=4, columnspan=3)

deck_box = ttk.Treeview(deck_tree_frame, columns=("Nb", "name", "format", "description", "Date_created"),
                              show='headings', selectmode='browse')
for nr, col_heading in enumerate(["Nb", "name", "format", "description", "Date_created"], 1):
    deck_box.column(f"# {nr}", anchor=W)
    deck_box.heading(f"# {nr}", text=col_heading, anchor=W)
deck_box.grid(row=8, columnspan=3)

##scrollbars
'''
collection_scroll = ttk.Scrollbar(collection_tree_frame, orient=VERTICAL, command=collection_scroll.yview)
collection_scroll.configure(yscroll=collection_scroll.set)
collection_scroll.grid(row=0, column=1, sticky='ns')

deck_scroll = ttk.Scrollbar(deck_tree_frame, orient=VERTICAL, command=deck_scroll.yview)
deck_scroll.configure(yscroll=deck_scroll.set)
deck_scroll.grid(row=0, column=1, sticky='ns')

'''


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

#query_database()

root.mainloop()




