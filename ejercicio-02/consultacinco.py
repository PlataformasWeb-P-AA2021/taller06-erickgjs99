from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del 
# archivo generar_base
from generar_base import Paises

# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite

engine = create_engine('sqlite:///basepaises.db')


Session = sessionmaker(bind=engine)
session = Session()


"""
Presentar todos los países que tengan en su cadena de nombre de país "uador" o en su cadena de capital "ito".
"""
print("--------------------------------")

consultaCinco = session.query(Paises).filter(or_(Paises.nombrePais.like("%uador%"), Paises.capital.like("%ito%"))).all()  
print(consultaCinco)

print("--------------------------------")