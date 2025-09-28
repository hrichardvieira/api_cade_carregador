from sqlalchemy import Column, String, Integer, ForeignKey

from model import Base

class City(Base) :
    __tablename__ = 'city'

    id_city = Column("id_city", Integer, primary_key=True)
    name = Column(String(140))
    id_state = Column(Integer, ForeignKey("state.id_state"), nullable=False)
    
    def __init__(self, name:str) :
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