def add_cardbyimage():
    ivest = str(input("Įveskite pilną kortos pavadinimą"))
    cards = Card.where(name=ivest).all()
    for card in cards:
        try:
            urllib.request.urlretrieve(f'{card.image_url}', "image.png")
        except ValueError:
            continue
    img = Image.open("image.png")
    img.show()
    print("Ar tai jūsų korta?\n 1-taip\n 2-ne")
    ivest1 = int(input(''))
    if ivest1 == 1:
        os.remove("image.png")
        ivest2 = int(input("Įveskite šios kortos kiekį"))
        for card in cards:
            try:
                a = card.type.split(' — ', 1)[0]
                b = type_check(remove_leg(a))
                card1= MTGcard(card.name, b, card.mana_cost, card.cmc, ivest2)
            except OperationalError:
                continue
        session.add(card1)
        session.commit()
        print("Korta pridėta")
    else:
        print("Pradėkite iš naujo")
        add_cardbyimage()

def type_check(arg):
    if arg == 'Land':
        return 1
    elif arg == 'Artifact':
        return 2
    elif arg == 'Creature':
        return 3
    elif arg == 'Enchantment':
        return 4
    elif arg == 'Instant':
        return 5
    elif arg == 'Planeswalker':
        return 6
    elif arg == 'Sorcery':
        return 7
    else:
        x = arg.split(' ', 1)
        type_check(x[1])

def remove_leg(arg):
    if arg.split(' ', 1)[0] == 'Legendary':
        return arg.split(' ', 1)[1]
    return arg