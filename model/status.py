from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from model import Base, Charger

class Status(Base) :
    __tablename__ = 'status'

    id_status = Column("id_status", Integer, primary_key=True)
    name = Column(String(140))
    
    def __init__(self, name:str) :
        """

        Registrar Status

        Arguments:
            name: Data de registro.
        
        """

        self.name = name

    def add_charger(self, charger:Charger) :
        """
            Adiciona carregador
        """

        self.charger.append(charger)