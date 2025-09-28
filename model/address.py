from sqlalchemy import Column, String, Integer, ForeignKey

from model import Base

class Address(Base) :
    __tablename__ = 'address'

    id_address = Column("id_address", Integer, primary_key=True)
    street = Column(String(140))
    id_neighborhood = Column(Integer, ForeignKey("neighborhood.id_neighborhood"), nullable=False)
    postal_code = Column(String(140))
    coordinates = Column(String(300))
    
    def __init__(self, street : str, id_neighborhood : int, postal_code : str, coordinates : str) :
        """Registrar o tipo do carregador

        Arguments:
            line: Data de registro
            output_current:
            charging_voltage:
            maximum_power:
            number_of_outlets:
            model:
        """

        self.street = street
        self.id_neighborhood = id_neighborhood
        self.postal_code = postal_code
        self.coordinates = coordinates