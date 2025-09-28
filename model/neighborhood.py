from sqlalchemy import Column, String, Integer, ForeignKey

from model import Base

class Neighborhood(Base) :
    __tablename__ = 'neighborhood'

    id_neighborhood = Column("id_neighborhood", Integer, primary_key=True)
    name = Column(String(140))
    id_city = Column(Integer, ForeignKey("city.id_city"), nullable=False)
    
    def __init__(self, name : str, id_city : int) :
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
        self.id_city = id_city