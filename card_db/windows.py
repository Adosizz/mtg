import sqlite3

conn = sqlite3.connect('models/MTG_card.db')
c = conn.cursor()
#with conn:
    #c.execute('''INSERT INTO Deck(Name, Format, description, Date_created)
     #           VALUES(elves, standart, elvesaggro,  2002-10-09)
    #''')

with conn:
    c.execute("SELECT * FROM Deck")
    records = c.fetchall()


print(records)
for record in records:
    print(record)
