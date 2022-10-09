from sqlalchemy import select
from models.card_db_model import session
from models.card_db_model import MtgCard, Type, Color




statement = select(MtgCard, Type, Color).join(Type).join(Color)
result = session.execute(statement).all()
print(result)
print(type(result))

for x in result:
    print(x)
