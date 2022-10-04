from tkinter import *

root = Tk()

root.title("Personal MTG database")
root.geometry("750x550")
root.resizable(False, False)





#main menu

mygt1 = Button(root, text="Cards")
mygt2 = Button(root, text="Decks")
mygt1.grid(row=0, column=0)
mygt2.grid(row=1, column=0)
root.mainloop()