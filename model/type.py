from sqlalchemy import Column, String, Integer, ForeignKey

from model import Base

class Type(Base) :
    __tablename__ = 'type'

    id_type = Column("id_type", Integer, primary_key=True)
    id_brand = Column(Integer, ForeignKey("brand.id_brand"), nullable=False)
    line = Column(String(140))
    output_current = Column(String(140))
    charging_voltage = Column(String(140))
    maximum_power = Column(String(140))
    number_of_outlets = Column(String(140))
    model = Column(String(140))

    
    def __init__(self, line:str, output_current:str, charging_voltage:str, maximum_power:str, number_of_outlets:str, model:str) :
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

        self.line = line
        self.output_current = output_current
        self.charging_voltage = charging_voltage
        self.maximum_power = maximum_power
        self.number_of_outlets = number_of_outlets
        self.model = model