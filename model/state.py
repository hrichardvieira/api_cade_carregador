from sqlalchemy import Column, String, Integer, ForeignKey

from model import Base

class State(Base) :
    __tablename__ = 'state'

    id_state = Column("id_state", Integer, primary_key=True)
    name = Column(String(140))
    fu = Column(String(2))
    id_country = Column(Integer, ForeignKey("country.id_country"), nullable=False)
    
    def __init__(self, name:str, fu:str) :
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
        self.fu = fu