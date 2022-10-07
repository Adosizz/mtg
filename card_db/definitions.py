from sqlalchemy.orm import sessionmaker
from models.card_db_model import engine, MtgCard, Type




Session = sessionmaker(bind=engine)
session = Session()



'''*************************************'''
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


def choose_type():
    ivest = input("Pasirinkite kortos tipo nr.:\n1-Land\n2-Artifact\n3-Creature\n"
                  "4-Enchantment\n5-Instant\n6-Sorcery")
    if ivest == 'Land' or ivest == '1':
        return 1
    elif ivest == 'Artifact' or ivest == '2':
        return 2
    elif ivest == 'Creature' or ivest == '3':
        return 3
    elif ivest == 'Enchantment' or ivest == '4':
        return 4
    elif ivest == 'Instant' or ivest == '5':
        return 5
    elif ivest == 'Planeswalker' or ivest == '6':
        return 6
    elif ivest == 'Sorcery' or ivest == '7':
        return 7


def add_manual():
    ivest = str(input("Įveskite kortos pavadinimą"))
    x_type = choose_type()
    x_manac = input("Įveskite kortos manos kainą.\n Pavyzdys: 2R(dvi betkokios ir viena raudona)\n B-Black\n "
                    "W-White\n R-Red\n "
                    "U-Blue\n G-Green")
    x_cmc= count_cmc(x_manac)
    ivest2 = int(input("Įveskite šios kortos kiekį"))
    card1 = MtgCard(ivest, x_type, x_manac, x_cmc, ivest2)
    session.add(card1)
    session.commit()
    print("Korta pridėta")

def count_cmc(arg):
    nr = '123456789'
    if arg[0] in nr:
        return int(arg[0]) + len(arg)-1
    else:
        return len(arg)

def filterby_type():
    x = choose_type()
    y=session.query(MtgCard).join(Type).filter(Type.id == x).all()
    for elem in y:
        print(elem.name, elem.mcost, elem.quant)

def show_cards():
    a = int(input("1-Rodyti visas kortas\n2Rodyti pasirinktą tipą"))
    if a == 1:
        y = session.query(MtgCard).all()
        for elem in y:
            print(elem.name, elem.mcost, elem.quant)
    else:
        filterby_type()

def main_menu():
    while True:
        x = int(input("Sveiki. Pasirinkite veiksmą\n1-Peržiūrėti jūsu kortas\n2-Pridėti kortą\n3-Koreguoti įrašus"))
        if x == 1:
            show_cards()
        elif x == 2:
            print("Pasirinkite kaip norite pridėti įrašą")
            z = int(input("1-Automatinis pridėjimas\n2 Rankinis pridėjimas"))
            if z == 1:
                add_cardbyimage()
            else:
                add_manual()
        #elif x == 3:



#main_menu()