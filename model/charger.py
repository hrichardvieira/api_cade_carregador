from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from typing import Union

from model import Base

class Charger(Base) :
    __tablename__ = 'charger'

    id_charger = Column("id_charger", Integer, primary_key=True)
    id_type = Column(Integer, ForeignKey("type.id_type"), nullable=False)
    id_address = Column(Integer, ForeignKey("address.id_address"), nullable=False)
    id_status = Column(Integer, ForeignKey("status.id_status"), nullable=False)
    name = Column(String(200))
    timestamp = Column(DateTime, default=datetime.now())
    
    def __init__(self, id_type : int, id_address : int, id_status : int, name : str, timestamp : Union[DateTime, None] = None) :
        """
        Registrar um carregador

        Arguments:
            id_type : id do tipo de carregador
            id_address : id do endereço que o carregador foi cadastrado 
            id_status : id do status do carregador
            name : nome do carregador
            timestamp : Data de registro.
        """
        self.id_type = id_type
        self.id_address = id_address
        self.id_status = id_status
        self.name = name

        if timestamp :
            self.timestamp = timestamp