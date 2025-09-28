from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from model import Base

class Brand(Base) :
    __tablename__ = 'brand'

    id_brand = Column("id_brand", Integer, primary_key=True)
    name = Column(String(140))
    
    def __init__(self, name:str) :
        """

        Registrar Brand

        Arguments:
            name: Data de registro.
        
        """

        self.name = name