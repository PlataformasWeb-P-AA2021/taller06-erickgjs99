from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from generar_base import Paises

import json, requests

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///basepaises.db')


Session = sessionmaker(bind=engine)
session = Session()

# se crean objetos de tipo Paises
# leer el archivo de datos

paisesData = requests.get("https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json")
json = (paisesData.json())

for d in json:
    p = Paises(nombrePais=d['CLDR display name'], capital=d['Capital'], continente=d['Continent'], \
            dial=d['Dial'], geonameId=d['Geoname ID'], itu=d['ITU'], lenguajes=d['Languages'], dependencia=d['is_independent'])
    session.add(p)

# confirmar transacciones

session.commit()
