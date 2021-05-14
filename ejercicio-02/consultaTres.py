
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
Presentar los lenguajes de cada país.
"""
print("--------------------------------")

paises = session.query(Paises).all()

for pais in paises:
    print("Pais: %s -> Lenguajes: %s" % (pais.nombrePais, pais.lenguajes))

print("--------------------------------")