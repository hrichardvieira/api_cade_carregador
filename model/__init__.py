from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

from model.base import Base
from model.address import Address
from model.brand import Brand
from model.charger import Charger
from model.city import City
from model.country import Country
from model.neighborhood import Neighborhood
from model.state import State
from model.status import Status
from model.type import Type

db_path = "database/"

if not os.path.exists(db_path) :
    os.makedirs(db_path)

db_url = 'sqlite:///%s/dbCarregador' % db_path

print(db_url)

engine = create_engine(db_url, echo=False)

Session = sessionmaker(bind=engine)

if not database_exists(engine.url):
    create_database(engine.url)

Base.metadata.create_all(engine)