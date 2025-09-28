from sqlalchemy import Column, String, Integer

from model import Base

class Country(Base) :
    __tablename__ = 'country'

    id_country = Column("id_country", Integer, primary_key=True)
    name = Column(String(140))
    country_code = Column(Integer)

    def __init__(self, name:str, country_code:int) :
        """

        Registrar o tipo do carregador

        Arguments:
            line: Data de registro
            output_current:
            charging_voltage:
            maximum_power:
            number_of_outlets:
            model:
        
        """

        self.name = name
        self.country_code = country_code